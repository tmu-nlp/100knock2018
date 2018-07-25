from sklearn.externals import joblib
import numpy as np
from knock82 import VOCAB_PATH, COOC_MAT_PATH

vocab = joblib.load(VOCAB_PATH).vocabulary_
cooc_mat = joblib.load(COOC_MAT_PATH)
print(np.sum(cooc_mat))
print(' '.join(vocab.keys()))

total = np.sum(cooc_mat)

while True:
    t,c = input('2 words:').strip().split()

    try:
        t = vocab[t.lower()]
    except:
        print('no such word:', t)
        continue
    try:
        c = vocab[c.lower()]
    except:
        print('no such word:', c)
        continue

    print('f(t,c) =', np.sum(cooc_mat[t,c]))
    print('f(t,*) =', np.sum(cooc_mat[t,:])) # axis = 1 to perserve axis 0
    print('f(*,c) =', np.sum(cooc_mat[:,c]), np.sum(cooc_mat, axis = 0)[0,c]) # axis = 0
