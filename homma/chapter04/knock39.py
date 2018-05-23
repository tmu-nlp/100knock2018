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

sorted_freq = sorted(frequency.values(), reverse=True)

plt.loglog(sorted_freq)
plt.show()


'''39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
'''
