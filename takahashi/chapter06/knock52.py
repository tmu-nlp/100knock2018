# -*- coding: utf-8 -*-
from stemming.porter2 import stem
from knock51 import *

def stemmed(file_name):
    for words in split_in_words(file_name):
        for word in words:
            stemmed_word = stem(word)
            yield word, stemmed_word


if __name__ == '__main__':
    file_name = '../data/nlp.txt'
    for word, stemmed_word in stemmed(file_name):
        print('\n'.join([word + '\t' + stemmed_word]))
