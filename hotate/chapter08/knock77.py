# -*- coding: utf-8 -*-
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib
from knock73 import make_data_x_y
import numpy as np


def accuracy():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    data_x, data_y = make_data_x_y()
    data_x = vectorizer.transform(data_x)
    data_y = np.array(data_y)
    label_true, label_pred = data_y, model.predict(data_x)
    print(classification_report(label_true, label_pred))
    print(f'accuracy = {accuracy_score(label_true, label_pred)}')


if __name__ == '__main__':
    accuracy()
