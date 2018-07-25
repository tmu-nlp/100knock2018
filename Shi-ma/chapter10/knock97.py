from sklearn.cluster import KMeans
import pickle

if __name__ == '__main__':
    with open('result/knock96.dump', 'rb') as data_in:
        labels_vecs = pickle.load(data_in)
        labels, vecs = list(map(lambda x: x[0], labels_vecs)), list(map(lambda x: x[1], labels_vecs))
        kmeans = KMeans(n_clusters=5)
        class_labels = kmeans.fit_predict(vecs)

        for class_label, label in sorted(zip(class_labels, labels)):
            print('{} : {}'.format(class_label, label))
