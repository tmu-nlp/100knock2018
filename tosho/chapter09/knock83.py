from sys import stdin, stdout
from random import randint, sample
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import numpy as np

def main():
    vectorizer = joblib.load('vocab.en')
    M_co = joblib.load('vocab.matrix')
    N = np.sum(M_co) // 2
    
    while True:
        t = input('input token: ').strip()
        c = input('input context token: ').strip()
        # t, c = 'types', 'and'

        tx = vectorizer.transform([t])
        cx = vectorizer.transform([c])

        tx = np.argmax(tx)
        cx = np.argmax(cx)

        ntc = M_co[tx, cx]
        nt = np.sum(M_co[tx])
        nc = np.sum(M_co[cx])

        print(f'{ntc} | {nt} | {nc} | {N}')


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')