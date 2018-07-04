# -*- coding: utf-8 -*-
from sklearn.metrics import precision_recall_curve
from sklearn.externals import joblib
from knock73 import make_data_x_y
import numpy as np
import matplotlib.pyplot as plt


def p_r_curve():
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
    data_x, data_y = make_data_x_y()
    data_x = vectorizer.transform(data_x)
    data_y = np.array(data_y)

    precision, recall, threshold = precision_recall_curve(data_y, model.predict_proba(data_x)[:, 1])

    plt.plot(precision, recall)
    plt.xlabel('Precision')
    plt.ylabel('Recall')

    plt.show()


if __name__ == '__main__':
    p_r_curve()
