# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-N', help='number of lines', default=0, type=int)
args = parser.parse_args()

line_count = 0
with open('../data/hightemp.txt', 'r', encoding="utf-8_sig") as f:
    for line in f:
        if line_count == args.N:
            break
        print(line.replace('\n', ''))
        line_count += 1