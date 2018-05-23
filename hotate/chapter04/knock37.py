# -*- coding: utf-8 -*-

from knock30 import load_mecab
from knock36 import morpheme_count
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def top_n(rank, n):
    x = []
    y = []
    fp = FontProperties(fname='/Users/hotate/Library/Fonts/ipaexg.ttf', size=14)

    for i, (morpheme, count) in enumerate(rank):
        if i > n - 1:
            break
        x.append(morpheme)
        y.append(count)
    plt.bar(x, y)
    plt.xticks(fontproperties=fp)
    plt.show()


if __name__ == '__main__':
    path = 'neko.txt.mecab'

    rank = sorted(morpheme_count(load_mecab(path)).items(), key=lambda x: -x[1])
    top_n(rank, 10)
