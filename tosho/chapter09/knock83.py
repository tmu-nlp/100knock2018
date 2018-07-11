from sys import stdin, stdout
from random import randint, sample
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import numpy as np

def main():
    vec = joblib.load('vocab.en')
    vocab = vec.vocabulary_
    co_matrix = joblib.load('co_matrix.lil')

    N = np.sum(co_matrix)
    
    while True:
        trg_word = input('input token: ').strip()
        ctx_word = input('input context token: ').strip()
    
        trg_id = vocab.get(trg_word)
        ctx_id = vocab.get(ctx_word)

        print(f't = {trg_word} (id:{trg_id})')
        print(f'c = {ctx_word} (id:{ctx_id})')

        nt = np.sum(co_matrix[trg_id, ])
        nc = np.sum(co_matrix.T[ctx_id, ])

        ntc = np.sum(co_matrix[trg_id, ctx_id])

        print(f'f(t,c) = {ntc} | f(t,*) = {nt} | f(*,c) = {nc} | N = {N}')


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')