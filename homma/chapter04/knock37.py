import matplotlib
from collections import defaultdict
from knock30 import load_morphems_iter
from matplotlib import pyplot as plt

# 日本語に対応させる
font = {'family': 'Kozuka Gothic Pro'}
matplotlib.rc('font', **font)
# 使えるFontの確認
# import matplotlib.font_manager as fm
# fonts = fm.findSystemFonts()
# for font in fonts: # fonts[:n] 先頭のn個
#     print(str(font), fm.FontProperties(fname=font).get_name())


frequency = defaultdict(int)
for m in load_morphems_iter():
    frequency[m['surface']] += 1

sorted_freq = list(sorted(frequency.items(), key=lambda x: -x[1]))

left   = [i for i in range(10)]
height = [s[1] for s in sorted_freq[:10]]
label  = [s[0] for s in sorted_freq[:10]]
plt.bar(left, height, tick_label=label, align='center')
plt.show()


'''37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
'''
