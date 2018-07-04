# -*- coding: utf-8 -*-
from sklearn.externals import joblib
from knock73 import  make_data_x_y


def pred_label(n):
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    data_x, data_y = make_data_x_y()
    text_vec = vectorizer.transform(data_x[:n])

    for text, label in zip(text_vec, data_y):
        print(f'{label}\t{model.predict(text)}\t{model.predict_proba(text)}')


if __name__ == '__main__':
    pred_label(15)
