import os,sys
sys.path.append(os.pardir)

from common.parsers import iterate_cabocha

def iterate_neko(filename='neko.txt.cabocha'):
    return iterate_cabocha(filename)

if __name__ == '__main__':
    from itertools import islice

    lines = list(islice(iterate_neko(),8))

    print(lines[0])

    line8 = lines[7]
    print(''.join(list(map(lambda c: c.sentence(), line8))))
        