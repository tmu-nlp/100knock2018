import xml.etree.ElementTree as ET
from re import compile as regex

mecab_fields_jp = ('品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用型', '活用形', '原形')#, '読み', '発音')
mecab_fields_en = ('POS', 'POS1', 'POS2', 'POS3', 'conjugative_form', 'conjugative_type', 'base_form')#, 'char_form', 'pronounce')
re_groups   = tuple(r'(?P<%s>[^,]+)' % fn for fn in mecab_fields_jp)
re_str      = ','.join(re_groups)
re_fields   = regex(re_str)

class Morph:
    def __init__(self, surface, feature):
        self._surface = surface
        self._feature = feature

    def __getattr__(self, name):
        if name in mecab_fields_jp:
            return self._feature.group(name)
        if name in mecab_fields_en:
            name = mecab_fields_jp[mecab_fields_en.index(name)]
            return self._feature.group(name)
        else:
            return self._surface

    def __str__(self):
        s = "'%s'\t%s"
        pos = []
        for i in mecab_fields_jp[:4]:
            p = eval(f'self.{i}')
            if p != '*':
                pos.append(p)
        pos = 'で'.join(pos)
        return s % (self._surface, pos)


def neko_root():
    s = ''
    with open('neko.xml') as fr:
        for line in fr:
            s += line
    s = '<book>%s</book>' % s
    return ET.fromstring(s)

if __name__ == '__main__':
    sent_cnt = 0
    for descendent in neko_root().getiterator():
        if descendent.tag == 'sentence': # bad 'is'
            sent_cnt += 1
            if sent_cnt > 3:
                break
        if sent_cnt == 3 and descendent.tag == 'tok': # bad 'is'
            tok = descendent
            m = Morph(tok.text, re_fields.match(tok.attrib['feature']))
            print(m)

# brew install
# https://qiita.com/musaprg/items/9a572ad5c4e28f79d2ae
