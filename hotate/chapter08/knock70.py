# -*- coding: utf-8 -*-
import random

list_ = []
for line in open('rt-polarity.pos', 'r', encoding='latin-1'):
    list_.append(f'+1 {line}')
for line in open('rt-polarity.neg', 'r', encoding='latin-1'):
    list_.append(f'-1 {line}')

random.shuffle(list_)

with open('sentiment.txt', 'w') as f:
    for line in list_:
        f.write(line)
