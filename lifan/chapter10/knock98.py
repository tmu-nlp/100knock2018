from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.externals import joblib
import matplotlib.pyplot as plt

def main():
  country_name_dict = joblib.load('country_name_dict.pkl')
  country_names = list(country_name_dict.keys())
  country_vectors = list(country_name_dict.values())
  result = linkage(country_vectors, method='ward')
  dendrogram(result, labels=country_names)
  plt.show()

if __name__ == '__main__':
  main()