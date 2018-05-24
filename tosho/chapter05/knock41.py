import os,sys
sys.path.append(os.pardir)

from common.parsers import iterate_cabocha
from itertools import islice

def iterate_neko(filename='neko.txt.cabocha'):
    return iterate_cabocha(filename)

def get_neko_chunks(n):
    return next(islice(iterate_neko(), n - 1, n))

if __name__ == '__main__':
    line8 = get_neko_chunks(8)

    for chunk in line8:
        o = chunk.sentence()
        if chunk.dst is not None:
            dst_chunk = line8[chunk.dst]
            o += ' -> ' + dst_chunk.sentence()
        print(o)