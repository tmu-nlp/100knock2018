# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-N', help='number of lines', default=0, type=int)
args = parser.parse_args()

records = []
with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        records.extend([line])

line_count = 0
if args.N > 0:
    for i in range(1, args.N+1):
        if line_count == args.N:
            break
        print(records[-i].replace('\n', ''))
        line_count += 1