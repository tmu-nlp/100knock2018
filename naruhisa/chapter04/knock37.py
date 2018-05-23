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
  labels = list()
  height = list()
  mpl.rcParams['font.family'] = 'AppleGothic'

  for count, k in enumerate(sorted(word_count.items(), key = lambda x:x[1], reverse = True)):
    if count == 10:
      break
    left.append(count+1)
    labels.append(k[0])
    height.append(k[1])
 
  plt.bar(left, height)
  plt.xticks(left, labels)
  plt.show()
