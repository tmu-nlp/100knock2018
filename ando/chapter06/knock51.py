import sys
import knock50

def wordsseparate():
    wordslist = []
    sentences = knock50.sentence()
    for i in sentences:
        words = i.strip().split(" ")
        wordslist.extend(words)
        wordslist.append(" ")
    return wordslist

if __name__ == "__main__":
    wordsseparate()