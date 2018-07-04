# -*- coding: utf-8 -*-
from sklearn.model_selection import cross_validate, StratifiedKFold
from sklearn.externals import joblib
from knock73 import make_data_x_y
import numpy as np


def kfold():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    data_x, data_y = make_data_x_y()
    data_x = vectorizer.transform(data_x)
    data_y = np.array(data_y)

    scoring = {
        'accuracy': 'accuracy',
        "precision": "precision",
        "recall": "recall",
        "f1": "f1"
    }

    skf = StratifiedKFold(n_splits=5, shuffle=True)

    scores = cross_validate(model, data_x, data_y, cv=skf, scoring=scoring)

    for key, value in scores.items():
        print(f'{key} : {value.mean()}')


if __name__ == '__main__':
    kfold()
