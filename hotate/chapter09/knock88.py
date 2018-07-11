# -*- coding: utf-8 -*-
from sklearn.externals import joblib
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def main():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    words = list(vocab.keys())
    england = pca[vocab['England']]
    eng_num = vocab['England']
    top = [[0, 0] for i in range(10)]
    for index, t in enumerate(pca):
        if index % 10000 == 0:
            print(index)
        cs = cosine_similarity(np.reshape(england, (1, -1)), np.reshape(t, (1, -1)))
        if cs > top[9][0] and index != eng_num:
            top[9][0] = cs
            top[9][1] = words[index]
            top.sort()
            top.reverse()
    print(top)


if __name__ == '__main__':
    main()

# [[array([[0.64690353]]), 'Scotland'], [array([[0.61430842]]), 'Australia'], [array([[0.57723432]]), 'Italy'],
#  [array([[0.57653445]]), 'France'], [array([[0.55961606]]), 'Germany'], [array([[0.55705794]]), 'Wales'],
# [array([[0.51807613]]), 'Spain'], [array([[0.51651049]]), 'Ireland'], [array([[0.50121334]]), 'United_Kingdom'],
# [array([[0.49918571]]), 'Britain']]
