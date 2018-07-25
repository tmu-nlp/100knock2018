'''
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
'''
import pickle
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE

with open('vec_countries', 'rb') as f:
    vec_countries = pickle.load(f)

list_vec_countries = []
list_countries = []
for country, vec in vec_countries.items():
    list_countries.append(country)
    list_vec_countries.append(vec)

tsne = TSNE().fit_transform(list_vec_countries)

fig, ax = plt.subplots()
ax.scatter(tsne[:, 0], tsne[:, 1], s=5)
for i, country in enumerate(list_countries):
    ax.annotate(country, xy=(tsne[i, 0], tsne[i, 1]), size=5)
plt.savefig('result99.png')