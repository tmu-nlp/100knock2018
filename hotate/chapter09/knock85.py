# -*- coding: utf-8 -*-
from sklearn.decomposition import TruncatedSVD
from sklearn.externals import joblib
from matplotlib import pyplot as plt


def main():
    ppmi = joblib.load('ppmi_mat.pkl')
    pca = TruncatedSVD(n_components=300)
    trans = pca.fit_transform(ppmi)
    plt.scatter(trans[:, 0], trans[:, 1])
    plt.title('principal component')
    plt.xlabel('pc1')
    plt.ylabel('pc2')
    print(pca.explained_variance_ratio_)
    plt.show()
    joblib.dump(trans, 'pca.pkl')


if __name__ == '__main__':
    main()
