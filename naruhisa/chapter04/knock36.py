from knock30 import *
from collections import defaultdict


if __name__ == '__main__':
  word_count = defaultdict(int)
  for sentence in ktskaiseki():
    for word in sentence:
      word_count[word['surface']] += 1

  for count, k in enumerate(sorted(word_count.items(), key = lambda x:x[1], reverse = True)):
    if count == 10:
      break
    print(k)
