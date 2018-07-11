# -*- coding: utf-8 -*-
from knock72 import tfidf_vectorizer, fit_vectorize
import random
from sklearn.externals import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression


def train():
    vectorizer = tfidf_vectorizer()
    data_x, data_y = make_data_x_y()
    train_x, train_y = make_train_data(vectorizer, data_x, data_y)
    model = LogisticRegression()
    model.fit(train_x, train_y)
    joblib.dump(vectorizer, 'vectorizer.pkl')
    joblib.dump(model, 'model.pkl')


def make_data_x_y():
    list_ = []
    for line in open('sentiment.txt', 'r'):
        list_.append(line.lower().strip())
    random.shuffle(list_)

    data_x = []
    data_y = []
    for line in list_:
        data_x.append(line[3:])
        data_y.append(int(line[:2]))
    return data_x, data_y


def make_train_data(vectorizer, data_x, data_y):
    data_x = fit_vectorize(data_x, vectorizer)
    data_y = np.array(data_y, dtype=int)
    return data_x, data_y


if __name__ == '__main__':
    train()
