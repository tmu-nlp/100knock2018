from gensim.models import word2vec
from scipy import io
import numpy as np
from bisect import bisect
import pickle


def spearman(array_x, array_y):
    N = len(array_x)

    return 1 - (6*sum((array_x - array_y)**2)) / (N**3 - N)


def create_rank_array(list_):
    rank_array = np.zeros(len(list_))
    sorted_list_ = sorted(list_)
    for i, element in enumerate(list_):
        rank_array[i] = len(list_) - bisect(sorted_list_, element) + 1

    return rank_array


def calc_spearman_data(data):
    human_list, word2vec_list = list(), list()
    for num_line, line in enumerate(data):
        if num_line == 0:
            continue
        cols = line.strip().split()
        human_list.append(cols[2])
        word2vec_list.append(cols[3])
    human_rank_array = create_rank_array(human_list)
    word2vec_rank_array = create_rank_array(word2vec_list)

    return spearman(human_rank_array, word2vec_rank_array)


if __name__ == '__main__':
    with open('result/knock94_85.txt', 'r') as data_in_85, open('result/knock94_90.txt', 'r') as data_in_90:
        print('knock85_spearman : {}'.format(calc_spearman_data(data_in_85)))
        print('knock90_spearman : {}'.format(calc_spearman_data(data_in_90)))


# 参照 #
# from scipy.stats import spearmanr のモジュールを用いれば簡単に計算できる
