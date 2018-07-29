from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import pickle

if __name__ == '__main__':
    with open('result/knock96.dump', 'rb') as data_in:
        labels_vecs = pickle.load(data_in)
        labels_, vecs = list(map(lambda x: x[0], labels_vecs)), list(map(lambda x: x[1], labels_vecs))

    tsne = TSNE(n_components=2, perplexity=60, learning_rate=230)
    tsne_result = tsne.fit_transform(vecs)

    kmeans = KMeans(n_clusters=5)
    class_labels = kmeans.fit_predict(vecs)

    for i in range(len(labels_)):
        plt.plot(tsne_result[i,0], tsne_result[i,1], ".", color=cm.prism(class_labels[i] / 4))

    plt.savefig('result/knock99.png')
