# -*- coding: utf-8 -*-
import sys

count = 0
with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        line = line.replace('\t', ' ')
        sys.stdout.write(line)
        print(line, end='\n')