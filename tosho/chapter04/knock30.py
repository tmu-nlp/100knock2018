import os,sys
sys.path.append(os.pardir)

from common.parsers import iterate_mecab_morphs

def parse_mecab(filename='neko.txt.mecab'):
    return list(iterate_mecab_morphs(filename))

if __name__ == '__main__':
    from random import sample

    data = parse_mecab()

    for item in sample(parse_mecab(),10):
        line = ''.join(map(lambda m : m.surface, item))
        print(line)
        for m in item:
            print(m)
        