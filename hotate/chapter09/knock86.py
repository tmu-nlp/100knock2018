# -*- coding: utf-8 -*-
from sklearn.externals import joblib


def main():
    pca = joblib.load('pca.pkl')
    vocab = joblib.load('vocab.pkl')
    count = 0
    for i, j in enumerate(pca):
        count = i
    print(count)
    united = pca[vocab['United_States']]
    print(united)


if __name__ == '__main__':
    main()
