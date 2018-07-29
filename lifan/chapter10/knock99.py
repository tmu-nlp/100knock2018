from sklearn.manifold import TSNE
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main():
  country_name_dict = joblib.load('country_name_dict.pkl')
  country_names = list(country_name_dict.keys())
  country_vectors = list(country_name_dict.values())
  result = TSNE(n_components=2, random_state=0).fit_transform(country_vectors)
  cluster_result = KMeans(n_clusters=5).fit(country_vectors)
  colors = ['grey', 'blue', 'red', 'purple', 'green']
  plt.figure(num=None, figsize=(16, 12), dpi=300)
  name = []
  for v in country_names:
    name.append(f'${v}$')
  for i, label in enumerate(cluster_result.labels_):
    plt.scatter(result[i, 0], result[i, 1], marker=name[i], s=200, c=colors[label])
  plt.show()

if __name__ == '__main__':
  main()
