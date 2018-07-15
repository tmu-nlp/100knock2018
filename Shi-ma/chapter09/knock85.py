from scipy.sparse import csr_matrix
from scipy import io
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import normalize
import numpy as np
import pickle



if __name__ == '__main__':
    X = io.loadmat('result/knock84_result.mat')['X']

    svd = TruncatedSVD(100)
    X_100 = svd.fit_transform(X)

    io.savemat('result/knock85_result.mat', {'X_100':X_100})