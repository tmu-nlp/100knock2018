# -*- coding: utf-8 -*-
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('-N', help='number of lines', default=0, type=int)
args = parser.parse_args()

records = []
with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        records.extend([line])

length = len(records)
if args.N == 0:
    line_num = 0
else:
    line_num = math.floor(length / float(args.N))

start = 0
end = line_num
if end > length:
    end = length

for i in range(args.N):
    with open('knock16_' + str(i) + '.txt', 'w', encoding='utf-8') as f:
        f.writelines(records[start:end])
    start = end
    end += line_num
    if end > length:
        end = length
