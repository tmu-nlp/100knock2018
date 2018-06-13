from knock30 import *
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib as mpl 

if __name__ == '__main__':
  word_count = defaultdict(int)
  for sentence in ktskaiseki():
    for word in sentence:
      word_count[word['surface']] += 1

  height = list()
  mpl.rcParams['font.family'] = 'AppleGothic'

  for k, v in sorted(word_count.items(), key = lambda x:x[1], reverse = True):
    height.append(v)
 
  plt.hist(height, bins = len(set(height)), log = True)
  plt.show()
