from sklearn.cluster import KMeans
from sklearn.externals import joblib
from collections import defaultdict
from pprint import pprint

def main():
  country_name_dict = joblib.load('country_name_dict.pkl')
  country_names = list(country_name_dict.keys())
  country_vectors = list(country_name_dict.values())
  cluster_result = KMeans(n_clusters=5).fit(country_vectors)
  labels = cluster_result.labels_
  clustred_country = defaultdict(list)
  for i, label in enumerate(labels):
    clustred_country[label].append(country_names[i])
  pprint(clustred_country)

if __name__ == '__main__':
  main()