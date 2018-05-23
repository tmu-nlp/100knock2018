# -*- coding: utf-8 -*-

from knock30 import load_mecab
from knock36 import morpheme_count
import matplotlib.pyplot as plt


def log_log_graph(rank):
    x = []
    y = []
    for i, (morpheme, count) in enumerate(rank):
        x.append(i+1)
        y.append(count)
    plt.scatter(x, y, s=10, marker='.')
    plt.yscale('log')
    plt.xscale('log')
    plt.show()


if __name__ == '__main__':
    path = 'neko.txt.mecab'
    rank = sorted(morpheme_count(load_mecab(path)).items(), key=lambda x: -x[1])
    log_log_graph(rank)
