#!/usr/bin/env bash

for i in {1..2}
do
    cut -d $'\t' -f $i < hightemp.txt > "col${i}.txt"
done
