# -*- coding: utf-8 -*-

count = 0
with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        line = line.replace('\t', ' ')
        print(line)