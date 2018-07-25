from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from pickle import load

with open('knock96.pkl', 'rb') as fr:
    countries = load(fr)

names = []
vectors = []
for k,v in countries.items():
    names.append(k)
    vectors.append(v)

r = linkage(vectors, method='ward')
dendrogram(r, labels = names)
plt.show()
