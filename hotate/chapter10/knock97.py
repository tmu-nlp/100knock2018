# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.externals import joblib


def cluster():
    vec = joblib.load('country_vec.pkl')
    country = joblib.load('country_dic.pkl')
    cls = KMeans(n_clusters=5).fit(vec)

    labels = cls.labels_

    for i, label in enumerate(labels):
        print(label, country[i])


if __name__ == '__main__':
    cluster()
