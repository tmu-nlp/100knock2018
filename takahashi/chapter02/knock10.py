# -*- coding: utf-8 -*-

count = 0
with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        count += 1
print(count)

with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    print(len(f.readlines()))
