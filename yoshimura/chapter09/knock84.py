'''
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ．ただし，行列Xの各要素Xtcは次のように定義する．

f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
f(t,c)<10ならば，Xtc=0
ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
'''
from tqdm import tqdm
from sklearn.externals import joblib
from scipy.sparse import lil_matrix
from scipy import io
import numpy as np
import pickle
import sys
import math

vocab = joblib.load('vocab')
vocab_size = len(vocab)

matrix = joblib.load('matrix')
matrix_ppmi = lil_matrix((vocab_size, vocab_size))

index = (matrix >= 10).nonzero()
t_idx, c_idx = index[0], index[1]
freq_t = np.sum(matrix, axis=1)
freq_c = np.sum(matrix, axis=1).reshape(vocab_size, 1)
N = np.sum(matrix)

for t, c in tqdm(zip(t_idx, c_idx)):
    ppmi = max(math.log((N * matrix[t, c]) / (freq_t[t] * freq_c[c])), 0) 
    matrix_ppmi[t, c] = ppmi

joblib.dump(matrix_ppmi, 'matrix_ppmi')