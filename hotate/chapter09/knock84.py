# -*- coding: utf-8 -*-
from scipy.sparse import lil_matrix
from sklearn.externals import joblib
import numpy as np
import math


def main():
    matrix = joblib.load('matrix.pkl')
    vocab = joblib.load('vocab.pkl')
    ppmi_mat = lil_matrix((len(vocab), len(vocab)))
    index = (matrix >= 10).nonzero()
    t_index = index[0]
    c_index = index[1]
    t_mat = np.sum(matrix, axis=1)
    c_mat = np.sum(matrix, axis=0).reshape(len(vocab), 1)
    N = np.sum(matrix)
    print(len(index))
    for i, (t, c) in enumerate(zip(t_index, c_index)):
        if i % 1000 == 0:
            print(i)
        ppmi = max(np.log((N * matrix[t, c]) / (t_mat[t] * c_mat[c])), 0)
        ppmi_mat[t, c] = ppmi

    joblib.dump(ppmi_mat, 'ppmi_mat.pkl')


if __name__ == '__main__':
    main()
