# -*- coding: utf-8 -*-
import numpy as np
from operator import itemgetter


def spearman(n, sum_):
    return 1 - (6 * sum_) / float(n ** 3 - n)


def dif_rank(h, p):
    sum_ = 0
    for x, y in zip(h, p):
        sum_ += (x - y) ** 2
    return sum_


def rank(path):
    rank_ = []
    for i, line in enumerate(open(path, 'r')):
        if i == 0:
            continue
        else:
            l = []
            line = line.strip().split()
            if line[3] == 'nan':
                continue
            l.append(float(line[2]))
            l.append(float(line[3]))
            rank_.append(l)
    rank_.sort(key=itemgetter(0))
    for i, r in enumerate(rank_):
        r.append(i + 1)
    rank_.sort(key=itemgetter(1))
    for i, r in enumerate(rank_):
        r.append(i + 1)
    return np.array(rank_)


def main():
    rank_pred_85 = rank('knock94_85.txt')
    rank_pred_90 = rank('knock94_90.txt')
    n = len(rank_pred_85[:, -2])
    print(spearman(n, dif_rank(rank_pred_85[:, -2], rank_pred_85[:, -1])))
    n = len(rank_pred_90[:, -2])
    print(spearman(n, dif_rank(rank_pred_90[:, -2], rank_pred_90[:, -1])))


if __name__ == '__main__':
    main()
