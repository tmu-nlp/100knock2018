from scipy.sparse import csr_matrix
from scipy import io
import numpy as np
import math
import pickle



if __name__ == '__main__':
    with open('result/knock83_result.dump', 'rb') as data_in:
        N, ids_t, ids_c, count_t, count_c, count_tc = pickle.load(data_in)

    row, col, data = [list() for i in range(3)]

    for tc in count_tc.keys():
        if count_tc[tc] >= 10:
            t, c = tc.split('___')
            if t == '' or c == '':
                continue
            row.append(ids_t[t])
            col.append(ids_c[c])
            data.append(max(math.log((N * count_tc[tc]) / (count_t[ids_t[t]] * count_c[ids_c[c]])), 0))

    X = csr_matrix((data, (row, col)), shape=(len(ids_t), len(ids_c)))
    io.savemat('result/knock84_result.mat', {'X':X})

# 参考 #
# 単語文書行列を作るときは DictVectorizer() を使うといい
