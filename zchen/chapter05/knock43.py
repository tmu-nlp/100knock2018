from knock41 import *
from knock42 import *

if __name__ == '__main__':
    for s in neko_sent().getchildren():
        sent = get_sentence(s)
        if sent is None:
            continue
        for c,d in get_dep(sent):
            if c.func == '名詞句' and d.func == '動詞句':
                print('%s\t%s' % (to_str(c),to_str(d)))
