from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt
import pickle

if __name__ == '__main__':
    with open('result/knock96.dump', 'rb') as data_in:
        labels_vecs = pickle.load(data_in)
        labels_, vecs = list(map(lambda x: x[0], labels_vecs)), list(map(lambda x: x[1], labels_vecs))

    Z = ward(vecs)

    dendrogram(Z, labels=labels_, leaf_font_size=2)
    plt.savefig('result/knock98.png', format = 'png', dpi=300)
