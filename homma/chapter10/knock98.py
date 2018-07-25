import pickle
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram


def main():
    data_path = 'knock96_country'
    with open(data_path, 'rb') as f:
        ids = pickle.load(f)
        vec = pickle.load(f)
    Z = linkage(vec, method='ward')
    plt.figure()
    dendrogram(Z, labels=list(ids.values()))
    plt.show()


if __name__ == '__main__':
    main()


''' 問
98. Ward法によるクラスタリング

96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
'''

''' 実行結果

'''
