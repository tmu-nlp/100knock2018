#!/usr/bin/env bash

filename='../data/hightemp.txt'
# タブ、スペースまとめて両方変えたい場合はsed
cat $filename | sed -e s/'¥t'/' '/
# お手軽なのはtr
cat $filename | tr ' ' '¥t'
# expandは置き換えるスペースの数を設定できる
cat $filename | expand -t 4