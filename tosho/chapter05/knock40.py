import os,sys
sys.path.append(os.pardir)

from common.parsers import iterate_mecab_morphs, iterate_cabocha

def iterate_neko(filename='neko.txt.cabocha'):
    return iterate_mecab_morphs(filename)

if __name__ == '__main__':
    from itertools import islice

    for item in islice(iterate_neko(),10):
        line = ''.join(map(lambda m : m.surface, item))
        print(line)
        for m in item:
            print(m)
        