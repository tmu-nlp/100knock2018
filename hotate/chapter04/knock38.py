# -*- coding: utf-8 -*-

from knock30 import load_mecab
from knock36 import morpheme_count
import matplotlib.pyplot as plt


def histogram(data):
    counts = []
    for morpheme, count in data.items():
        counts.append(count)
    plt.hist(counts, bins=20, range=(1, 50))
    plt.show()


if __name__ == '__main__':
    path = 'neko.txt.mecab'
    histogram(morpheme_count(load_mecab(path)))


