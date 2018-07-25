from sklearn.cluster import KMeans
from collections import defaultdict
from pickle import load
from pprint import pprint

with open('knock96.pkl', 'rb') as fr:
    countries = load(fr)

names = []
vectors = []
for k,v in countries.items():
    names.append(k)
    vectors.append(v)

r = KMeans(n_clusters=5).fit(vectors)
cluster = defaultdict(list)
for name_id, cluster_id in enumerate(r.labels_):
    cluster[cluster_id].append(names[name_id])

pprint(cluster)
