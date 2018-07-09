from knock71 import *
import copy
from nltk import stem
from collections import defaultdict

def sosei():
    stemmer2 = stem.LancasterStemmer()
    ids = defaultdict(lambda: len(ids))
    for line in open("sentiment.txt").readlines():
        line = line.split()
        for word in line.pop(0):
            ids[stemmer2.stem(word)]
    stop = []
    for line in open("stop.txt","r"):
        stop.append(line.strip())
    sosei_list = []
    label_list = []
    for line in open("sentiment.txt","r"):
        line = line.split()
        label = line[0]
        line = line.pop(0)
        line2 = copy.deepcopy(line)
        for word in line:
            if stop_check(word,stop):
                line2.remove(word)
        line = [0]*len(ids)
        for word in line2:
            line[ids[stemmer2.stem(word)]] += 1
        sosei_list.append(line)
        label_list.append(label)
    return label_list,sosei_list


if __name__ == "__main__":
    sosei()