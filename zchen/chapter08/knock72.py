from knock71 import Corpus
import numpy as np
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer


def vectorize(vectorizer = TfidfVectorizer):
    corp = Corpus()
    data = tuple(corp.hand_engineering())
    X, Y = zip(*data)
    Y = np.asarray(Y)
    X = [' '.join(x) for x in X]
    vecor = vectorizer() # tokenizer
    X = vecor.fit_transform(X)
    return vecor, X, Y
    # vocab = defaultdict(lambda:len(vocab))
    # sign_X = []
    # for toks in X:
    #     sign_X.append(tuple(vocab[tok] for tok in toks))
    # self.X = np.zeros((len(sign_X), len(vocab)))
    # print('Vocab size:', len(vocab))
    # for i, toks in enumerate(sign_X):
    #     for j in toks:
    #         self.X[i,j] = 1
    # self.vocab = vocab

if __name__ == '__main__':
    vectorize()
