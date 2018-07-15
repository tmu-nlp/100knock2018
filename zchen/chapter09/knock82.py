import pdb
import numpy as np
import scipy.sparse as smat
from sklearn.feature_extraction.text import CountVectorizer
from random import randint
#from itertools import chain # chain(*list)
from knock80 import *
from knock81 import *
from sklearn.externals import joblib
#from multiprocessing import Pool
from pathos.multiprocessing import ProcessingPool as Pool
from tqdm import tqdm
from argparse import ArgumentParser
import bz2

VOCAB_PATH = 'vocab.joblib'
TEXT_PATH = 'text.bz'
COOC_MAT_PATH = 'cooc_mat.joblib'

# bsr_matrix: Block Sparse Row (compressed vs. csr)
#    (data, (row_idx, col_idx), blockize(r, c)) r % R == c % C == 0
#    (data, indices, indptr)
#        col_idx = indices[indptr[i]:indptr[i+1]]
#        data    = data   [indptr[i]:indptr[i+1]]
# coo_matrix: COOrdinate format
#    'ijv' or triplet format
#    cost for ij
#    cumulative version of dok_matrix
# csc_matrix: csr_matrix: Compressed Sparse Column|Row
# indptr: [0 2 3 6] <- row divider, len(indptr) + 1 == dense.nrow
#  0 1 2 3 4 5 6
#  + + | |     |
#      + |     |
#        + + + |
# [0 2|2|0 1 2] col_idx
# [1 2 3 4 5 6] data
#    [[1 0 2] <-- todense/toarray
#     [0 0 3]
#     [4 5 6]]
# dia_matrix: DIAgonal storage
#       dig.todense()  idx   data
#    -2-1 [ 0 1 2]       0 [[ 0 0 0]
#      -2 [-1 0 1] 2     1  [ 1 1 ?]
#         [-2-1 0] 1 2  -1  [ ?-1-1]]
# dok_matrix: Dict Of Keys
#    'ijv' format plant
#    cost for ij
# lil_matrix: Linked List (Row-based)
#    append o(0) but...
# spmatrix: base class
#
# chinese ref:
# https://www.cnblogs.com/zhangchaoyang/articles/5483453.html

def window_slicer(abs_i, b, max_len):
    l = abs_i - b
    if l < 0:
        lc = 0
        c = abs_i
    else:
        lc = l
        c = b
    cr = min(max_len, abs_i + b + 1)
    return slice(lc, cr), c

def word_context_gen(line, rand = False, win_span = 5):
    max_len = len(line)
    for i, tok in enumerate(line):
        b = randint(1, win_span) if rand else win_span
        s, c = window_slicer(i, b, max_len)
        context = line[s]
        word = context.pop(c)
        yield word, context

def save_to():
    compound_list = list(load_countries(True))
    trie = make_trie(compound_list)

    docs = ''
    for toks in load_lines():
        docs += ' '.join(combine_compound(toks, trie)) + '\n'

    with bz2.open(TEXT_PATH, 'wb') as fw:
        fw.write((s).encode('utf-8'))

    cv = CountVectorizer(stop_words = []) # None doesn't work
    cv.fit(docs) # we don't need _transform()
    joblib.dump(cv, VOCAB_PATH)

def mp(tup):
    idx, (dim, analyzer, vocab), lines = tup
    cooc_mat = smat.dok_matrix((dim, dim), dtype = np.uint) # dok is faster at small amount
    # smat suggest to use lil, csr(3it/s), dok(100->6), lil(150)
    for line in tqdm(lines, desc = 'proc %d' % idx):
        line = [vocab[w] for w in analyzer(line)]
        for w, c in word_context_gen(line, rand = True, win_span = 5):
            for s in c:
                cooc_mat[w, s] += 1
    return cooc_mat

def make_cooc_mat(num_procs = 4):
    cv = joblib.load(VOCAB_PATH)
    pool = Pool(num_procs)
    analyzer = cv.build_analyzer()
    vocab = cv.vocabulary_
    dim = len(cv.vocabulary_)
    shared_params = dim, analyzer, vocab
    print('vocab size:', dim)
    cooc_mat = np.zeros((dim, dim), dtype = np.uint)
    sub_lines = []
    sub_blocks = []
    for line in bz2_line_gen(TEXT_PATH):
        if len(sub_lines) < 10000:
            sub_lines.append(line)
        elif len(sub_blocks) < num_procs:
            sub_blocks.append((len(sub_blocks), shared_params, sub_lines))
            sub_lines = []
        else:
            for cooc in pool.uimap(mp, sub_blocks):
                cooc_mat += cooc
            sub_blocks = []
            print('block')
    joblib.dump(cooc_mat, COOC_MAT_PATH)

def _test0():
    for i in range(5):
        print(window_slicer(i, 2, 5))

def _test1():
    s = 'a b c d e'.split()
    v = {t:i for i,t in enumerate(s)}
    for w,c in word_context_gen(s, v, rand = True, win_span = 2):
        print(w, c)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-m', '--mode')
    args = parser.parse_args()
    if args.mode == 'vocab':
        save_to()
    elif args.mode == 'mat':
        make_cooc_mat()
    #import cProfile
    #cProfile.run('')
