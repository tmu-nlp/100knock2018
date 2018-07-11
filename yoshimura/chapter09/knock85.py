'''
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，単語の意味ベクトルを300次元に圧縮せよ．
'''
from sklearn.externals import joblib
from sklearn import decomposition

# 読み込み
matrix_ppmi = joblib.load('matrix_ppmi')
svd = decomposition.TruncatedSVD(300)
matrix_300 = svd.fit_transform(matrix_ppmi)
joblib.dump(matrix_300, 'matrix_300')

