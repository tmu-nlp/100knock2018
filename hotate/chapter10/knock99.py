# -*- coding: utf-8 -*-
from sklearn.manifold import TSNE
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def tsne():
    vec = joblib.load('country_vec.pkl')
    country = joblib.load('country_dic.pkl')
    result = TSNE(n_components=2, random_state=0).fit_transform(vec)
    cls = KMeans(n_clusters=6).fit(vec)
    colors = ['red', 'blue', 'yellow', 'pink', 'green', 'cyan']
    plt.figure(num=None, figsize=(16, 12), dpi=300)

    name = []
    for v in country.values():
        name.append(f'${v}$')
    for i, label in enumerate(cls.labels_):
        plt.scatter(result[i, 0], result[i, 1], marker=name[i], s=2000, c=colors[label])
    plt.show()


if __name__ == '__main__':
    tsne()
