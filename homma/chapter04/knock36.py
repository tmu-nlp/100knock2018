from knock30 import load_morphems_iter
from collections import defaultdict

frequency = defaultdict(int)
for m in load_morphems_iter():
    frequency[m['surface']] += 1

sorted_freq = list(sorted(frequency.items(), key=lambda x: -x[1]))

print(sorted_freq)


'''36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
'''
