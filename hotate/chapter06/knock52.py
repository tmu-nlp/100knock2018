# -*- coding: utf-8 -*-

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

if __name__ == '__main__':
    for word in open('knock51.txt', 'r'):
        word = word.strip('\n')
        print(f'{word}\t{ps.stem(word)}')
