# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    with open('knock51.txt', 'w') as f:
        for line in open('knock50.txt', 'r'):
            line = line.strip('\n').split()
            for i, word in enumerate(line):
                print(word, file=f)
                if i == len(line)-1:
                    print(file=f)
