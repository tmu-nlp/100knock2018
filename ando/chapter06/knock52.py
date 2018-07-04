import sys
import knock51
from stemming.porter2 import stem

def stemize():
    words = knock51.wordsseparate()
    pair = []
    for word in words:
        pair.append((word,stem(word)))

if __name__ == "__main__":
    stemize()