# -*- coding: utf-8 -*-
from sklearn.externals import joblib


def weight_rank():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')

    ids = vectorizer.get_feature_names()
    weight = model.coef_[0].tolist()
    pair = list(zip(weight, ids))
    pair.sort()

    print(pair[:10])
    print(pair[:-11:-1])


if __name__ == '__main__':
    weight_rank()
