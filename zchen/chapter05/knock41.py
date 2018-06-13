from knock40 import *
from sys import argv

class Chunk:
    def __init__(self, chunk):
        cm = []
        for tok in chunk.getchildren():
            m = Morph(tok.text, tok.attrib['feature'])
            if chunk.attrib['head'] == tok.attrib['id']:
                self._head = m.品詞 + '句'
            if chunk.attrib['func'] == tok.attrib['id']:
                self._func = m.品詞 + '句'
            cm.append(m)
        self.morphs = cm
        self.dep_on = None
        self.dep_by = []

    @property
    def func(self):
        return self._func

    @property
    def head(self):
        return self._head

    def __str__(self):
        s = self._func
        c = self.c_str()
        if c:
            s = f"{s}({c})"
        m = self.m_str()
        if m:
            s = f"{s}[{m}]"
        return s

    def m_str(self, sep = '|', no_punc = False):
        if no_punc:
            return sep.join(m.surface for m in self.morphs if m.品詞 != '記号')
        return sep.join(m.surface for m in self.morphs)

    def c_str(self, sep = ';'):
        return sep.join(str(c) for c in self.dep_by)

def get_sentence(sent):
    cs = []
    for chunk in sent.getchildren():
        c = Chunk(chunk)
        d = int(chunk.attrib['link'])
        cs.append((c, d))
    tc = None
    for c, d in cs:
        if d < 0:
            tc = c
            continue
        c.dep_on = cs[d][0]
        cs[d][0].dep_by.append(c)
    return tc


if __name__ == '__main__':
    sent = get_sentence(neko_sent(int(argv[1])))
    print(sent)
