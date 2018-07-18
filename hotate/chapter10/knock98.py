# -*- coding: utf-8 -*-
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.externals import joblib
import matplotlib.pyplot as plt


def cls_ward():
    vec = joblib.load('country_vec.pkl')
    country = joblib.load('country_dic.pkl')
    result = linkage(vec, method='ward')
    plt.figure(num=None, figsize=(16, 9), dpi=300)
    dendrogram(result, labels=list(country.values()))
    plt.show()


if __name__ == '__main__':
    cls_ward()
