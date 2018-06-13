import xml.etree.ElementTree as ET
from re import compile as regex

mecab_fields_jp = ('品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用型', '活用形', '原形', '読み', '発音')
mecab_fields_en = ('POS', 'POS1', 'POS2', 'POS3', 'conjugative_form', 'conjugative_type', 'base_form', 'char_form', 'pronounce')

class Morph:
    def __init__(self, surface, feature):
        self._surface = surface
        self._feature = feature.split(',')

    def __getattr__(self, name):
        if name in mecab_fields_jp:
            idx = mecab_fields_jp.index(name)
        elif name in mecab_fields_en:
            idx = mecab_fields_en.index(name)
        else:
            return self._surface
        return self._feature[idx]

    def __str__(self):
        s = "'%s'\t%s"
        pos = []
        for i in mecab_fields_jp[:4]:
            p = eval(f'self.{i}')
            if p != '*':
                pos.append(p)
        pos = 'で'.join(pos)
        return s % (self._surface, pos)


def neko_sent(idx = None):
    s = ''
    sent_cnt = -1
    reading = False
    with open('neko.xml') as fr:
        for line in fr:
            if idx:
                if line.startswith('<sentence>'):
                    sent_cnt += 1
                if sent_cnt < idx:
                    continue
                else:
                    reading = True

                if reading:
                    s += line
                    if line.startswith('</sentence>'):
                        break

            else:
                s += line
    if idx:
        return ET.fromstring(s)
    s = '<book>%s</book>' % s
    return ET.fromstring(s)

if __name__ == '__main__':
    for descendent in neko_sent(2).getiterator():
        if descendent.tag == 'tok': # bad 'is'
            tok = descendent
            m = Morph(tok.text, tok.attrib['feature'])
            print(m)

# brew install
# https://qiita.com/musaprg/items/9a572ad5c4e28f79d2ae
