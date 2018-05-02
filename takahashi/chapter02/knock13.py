# -*- coding: utf-8 -*-

line_count = 0
col1_line = []
col2_line = []
with open('col1.txt', 'r', encoding="utf-8") as f:
    for line in f:
        col1_line.append(line)

with open('col2.txt', 'r', encoding="utf-8") as f:
    for line in f:
        col2_line.append(line)

with open('knock13.txt', 'w', encoding='utf-8') as f:
    f.writelines(col1_line)
    f.writelines(col2_line)
