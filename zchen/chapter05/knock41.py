from knock40 import *

class Chunk:
    def __init__(self, chunk):
        cm = []
        for tok in chunk.getchildren():
            res = re_fields.match(tok.attrib['feature'])
            pos = res.group('品詞')
            if chunk.attrib['head'] == tok.attrib['id']:
                self._head = pos + '句'
            m = Morph(tok.text, res)
            cm.append(m)
        self._morphs = cm
        self.dep_on = None
        self.dep_by = []

    @property
    def head(self):
        return self._head

    def __str__(self):
        s = self._head
        c = self.c_str()
        if c:
            s = f"{s}({c})"
        m = self.m_str()
        if m:
            s = f"{s}[{m}]"
        return s

    def m_str(self, no_punc = False):
        if no_punc:
            return '|'.join(m.surface for m in self._morphs if m.品詞 != '記号')
        return '|'.join(m.surface for m in self._morphs)

    def c_str(self):
        return ';'.join(str(c) for c in self.dep_by)

def get_sentence():
    sents = []
    for sent in neko_root().getchildren():
        cs = []
        for chunk in sent.getchildren():
            c = Chunk(chunk)
            d = int(chunk.attrib['link'])
            cs.append((c, d))
        for c, d in cs:
            if d < 0:
                tc = c
                continue
            c.dep_on = cs[d][0]
            cs[d][0].dep_by.append(c)

        sents.append(tc if cs else None)
    return sents


if __name__ == '__main__':
    sents = get_sentence()[:8]
    for s in sents:
        print(s)
