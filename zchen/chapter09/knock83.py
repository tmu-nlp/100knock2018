from sklearn.externals import joblib
import numpy as np
from knock82 import VOCAB_PATH, COOC_MAT_PATH

vocab = joblib.load(VOCAB_PATH)
cooc_mat = joblib.load(COOC_MAT_PATH)

total = np.sum(cooc_mat)

while True:
    t,c = input('2 words:').strip().split()

    try:
        t = vocab[t]
    except:
        print('no such word:', t)
        continue
    try:
        c = vocab[c]
    except:
        print('no such word:', c)
        continue

    nt  = np.sum(cooc_mat[t, ])
    nc  = np.sum(cooc_mat.T[c, ])
    ntc = np.sum(cooc_mat[t, c])

    print(f'f(t,c) = {ntc} | f(t,*) = {nt} | f(*,c) = {nc} | f(*,*) = {total}')
