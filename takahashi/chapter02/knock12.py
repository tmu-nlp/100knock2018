# -*- coding: utf-8 -*-

line_count = 0
col1 = []
col2 = []

with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        line = line.split()
        col1.append(line[0])
        col2.append(line[1])
    with open('col1.txt', 'w', encoding='utf-8') as wf:
        for item in col1:
            wf.write(item + '\n')
    with open('col2.txt', 'w', encoding='utf-8') as wf:
        for item in col2:
            wf.write(item + '\n')
