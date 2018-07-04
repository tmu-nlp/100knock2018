# -*- coding: utf-8 -*-
from sklearn.externals import joblib
from knock73 import make_data_x_y


def test(n):
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    data_x, data_y = make_data_x_y()
    text_vec = vectorizer.transform(data_x[:n])

    for vec, text in zip(text_vec, data_x):
        print(f'入力文 : {text.strip()}')
        print(f'予測結果 : {model.predict(vec)}')
        print(f'予測確率 : {model.predict_proba(vec)}')
        print()


if __name__ == '__main__':
    test(5)
