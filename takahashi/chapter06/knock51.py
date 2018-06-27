# -*- coding: utf-8 -*-

from knock50 import *

def split_in_words(file_name):
    for line in nlp_lines(file_name):
        words = line.split(' ')
        yield words


if __name__ == '__main__':
    file_name = '../data/nlp.txt'
    for words in split_in_words(file_name):
        print('\n'.join(words))

