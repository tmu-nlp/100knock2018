# -*- coding: utf-8 -*-
from sklearn.externals import joblib
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def main():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    words = list(vocab.keys())
    vec = pca[vocab['Spain']] - pca[vocab['Madrid']] + pca[vocab['Athens']]
    top = [[0, 0] for i in range(10)]
    for index, t in enumerate(pca):
        if index % 10000 == 0:
            print(index)
        cs = cosine_similarity(np.reshape(vec, (1, -1)), np.reshape(t, (1, -1)))
        if cs > top[9][0]:
            top[9][0] = cs
            top[9][1] = words[index]
            top.sort()
            top.reverse()
    print(top)

def sim():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    norm = np.linalg.norm(pca, ord=2, axis=1)
    pca = pca / norm[:, np.newaxis]
    words = list(vocab.keys())
    vec = pca[vocab['Spain']] - pca[vocab['Madrid']] + pca[vocab['Athens']]
    top = [[0, 0] for i in range(10)]
    for index, t in enumerate(pca):
        if index % 10000 == 0:
            print(index)
        result = np.dot(pca[index], vec)
        if result > top[9][0]:
            top[9][0] = result
            top[9][1] = words[index]
            top.sort()
            top.reverse()
    print(top)


if __name__ == '__main__':
    main()
    sim()

# [[array([[0.86879466]]), 'Spain'], [array([[0.77158251]]), 'Italy'], [array([[0.76376002]]), 'Austria'],
#  [array([[0.76037371]]), 'Sweden'], [array([[0.74444281]]), 'France'], [array([[0.73941769]]), 'Netherlands'],
# [array([[0.73808361]]), 'Germany'], [array([[0.7004954]]), 'Belgium'], [array([[0.69737437]]), 'Denmark'],
# [array([[0.69105679]]), 'Télévisions']]
