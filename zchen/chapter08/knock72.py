from knock71 import check
import numpy as np
from collections import defaultdict


class FeatMat:
    def __init__(self):
        X, Y = tuple(check())
        self.Y = np.asarray(Y)
        vocab = defaultdict(lambda:len(vocab))
        sign_X = []
        for toks in X:
            sign_X.append(tuple(vocab[tok] for tok in toks))
        self.X = np.zeros((len(sign_X), len(vocab)))
        for i, toks in enumerate(sign_X):
            for j in toks:
                self.X[i,j] = 1
        self.vocab = vocab

if __name__ == '__main__':
    fm = FeatMat()
