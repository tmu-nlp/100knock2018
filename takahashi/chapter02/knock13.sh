#!/usr/bin/env bash

filename='../data/hightemp.txt'
col1='col1.txt'
col2='col2.txt'

# -sを指定すると、全ての行を1行にまとめる
# -dでデリミタを指定する。デフォルトはタブ
paste $col1 $col2 > $filename