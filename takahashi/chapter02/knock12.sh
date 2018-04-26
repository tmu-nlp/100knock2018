#!/usr/bin/env bash

filename='../data/hightemp.txt'
col1='col1.txt'
col2='col2.txt'
# -fで取得したいフィールドを設定する
# -dでデリミタを指定する。-fも設定する必要がある
cut -d , -f 1 < $filename > $col1
cut -d , -f 2 < $filename > $col2