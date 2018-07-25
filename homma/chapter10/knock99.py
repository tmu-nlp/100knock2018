import pickle
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans


def main():
    data_path = 'knock96_country'
    with open(data_path, 'rb') as f:
        ids = pickle.load(f)
        vec = pickle.load(f)
    tsne = TSNE().fit_transform(vec)
    cls = KMeans(6).fit(vec)
    plt.figure()

    names = [f'${n}$' for n in ids.values()]
    for i, (label, n) in enumerate(zip(cls.labels_, names)):
        plt.scatter(tsne[i, 0], tsne[i, 1], marker=n)
    plt.show()


if __name__ == '__main__':
    main()


''' 問
99. t-SNEによる可視化

96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
'''

''' 実行結果

'''
