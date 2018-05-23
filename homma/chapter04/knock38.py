import matplotlib
import numpy as np
from collections import defaultdict
from knock30 import load_morphems_iter
from matplotlib import pyplot as plt

# 日本語に対応させる
font = {'family': 'Kozuka Gothic Pro'}
matplotlib.rc('font', **font)


frequency = defaultdict(int)
for m in load_morphems_iter():
    frequency[m['surface']] += 1

plt.hist(list(frequency.values()), bins=100)
plt.show()


'''38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
'''
