import pickle
from scipy import io
from sklearn.decomposition import PCA
# https://stackoverflow.com/questions/33603787/performing-pca-on-large-sparse-matrix-by-using-sklearn


def main():
    # 読み込み
    ppmi_mat = io.loadmat('ppmi_mat')['ppmi_mat']
    # 次元圧縮
    # pca = TruncatedSVD(n_components=300)
    pca = PCA(n_components=300)
    # ppmi_mat_300 = pca.fit_transform(ppmi_mat) # ppmi_mat.todense()でやればPCAでできる
    ppmi_mat_300 = pca.fit_transform(ppmi_mat.todense())
    # 保存
    io.savemat('knock85_300', {'ppmi_mat_300': ppmi_mat_300})

if __name__ == '__main__':
    main()


''' 問
85. 主成分分析による次元圧縮

84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
'''

''' 実行結果

'''
