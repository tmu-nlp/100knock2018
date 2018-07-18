from collections import defaultdict
import numpy as np
import pickle
from tqdm import tqdm



def create_ids(data, ids_t, ids_c):
    for line in data:
        t, c = line.strip().split('\t')
        ids_t[t]
        ids_c[c]


if __name__ == '__main__':
    with open('result/knock82_result.txt', 'r') as data_in:
        ids_t = defaultdict(lambda: len(ids_t))
        ids_c = defaultdict(lambda: len(ids_c))
        create_ids(data_in, ids_t, ids_c)

    with open('result/knock83_result.dump', 'wb') as data_out:
        N = 0
        count_t = np.zeros(len(ids_t))
        count_c = np.zeros(len(ids_c))
        count_tc = defaultdict(lambda: 0)
        for line in tqdm(open('result/knock82_result.txt', 'r')):
            N += 1
            t, c = line.strip().split('\t')
            count_t[ids_t[t]] += 1
            count_c[ids_c[c]] += 1
            count_tc[t + '___' + c] += 1

        pickle.dump([N, dict(ids_t), dict(ids_c), count_t, count_c, dict(count_tc)], data_out)

# 参考 #
# Counter() を使うと良い
