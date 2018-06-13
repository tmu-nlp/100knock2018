from knock30 import *
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib as mpl 

if __name__ == '__main__':
  word_count = defaultdict(int)
  for sentence in ktskaiseki():
    for word in sentence:
      word_count[word['surface']] += 1

  left = list()
  height = list()
  mpl.rcParams['font.family'] = 'AppleGothic'

  for count, k in enumerate(sorted(word_count.items(), key = lambda x:x[1], reverse = True)):
    left.append(count+1)
    height.append(k[1])

  plt.xscale('log')
  plt.yscale('log') 
  plt.bar(left, height)
  plt.show()
