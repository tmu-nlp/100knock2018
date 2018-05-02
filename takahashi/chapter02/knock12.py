# -*- coding: utf-8 -*-

line_count = 0
with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        if line_count == 0:
            with open('col1.txt', 'w', encoding='utf-8') as wf:
                wf.write(line)
        elif line_count == 1:
            with open('col2.txt', 'w', encoding='utf-8') as wf:
                wf.write(line)
        line_count += 1