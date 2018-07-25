from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from pickle import load

with open('knock96.pkl', 'rb') as fr:
    countries = load(fr)

names = []
vectors = []
for k,v in countries.items():
    names.append(k)
    vectors.append(v)

r_tsne = TSNE(n_components = 2, random_state = 0).fit_transform(vectors)
r_clsr = KMeans(n_clusters = 5).fit(vectors)
plt.figure(num=None, figsize=(16, 12), dpi=300)
name = []
for v in names:
    name.append(f'${v}$')
colors = ['grey', 'blue', 'red', 'purple', 'green']
for name_id, cluster_id in enumerate(r_clsr.labels_):
    plt.scatter(r_tsne[name_id, 0], r_tsne[name_id, 1], marker = name[name_id], s = 200, c = colors[cluster_id])
plt.show()
