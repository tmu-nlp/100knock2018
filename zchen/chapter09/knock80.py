import bz2
#from re import compile as regex
from tqdm import tqdm
_p = '.,!?;:()[\]\'"'
#_punc = regex(f'(^[{_p}]+|(?<!\.\w)[{_p}]+$)')

def load_lines(fname = 'enwiki-20150112-400-r10-105752.txt.bz2'):
    for cnt, line in enumerate(bz2_line_gen(fname)):
        if line == '':
            continue
        if cnt > 100:
            break
        line = (tok.strip(_p) for tok in line.split(' '))
        yield [w for w in line if w]

def bz2_line_gen(fname):
    with bz2.open(fname) as fr:
        for line in tqdm(fr, desc = 'read'):
            yield line.decode('utf-8').rstrip()
