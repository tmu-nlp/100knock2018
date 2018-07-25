'''
98. Ward法によるクラスタリング
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
'''

import pickle
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt

with open('vec_countries', 'rb') as f:
    vec_countries = pickle.load(f)

list_vec_countries = []
list_countries = []
for country, vec in vec_countries.items():
    list_countries.append(country)
    list_vec_countries.append(vec)

ward = ward(list_vec_countries)
dendrogram(ward, labels=list_countries)
plt.show()