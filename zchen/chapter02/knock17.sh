#!/usr/bin/env bash

# line is the unit for sort by default
# unique/set will never be made without sort
# check more by examples in that book
cut -d $'\t' -f 1 "hightemp.txt" | sort | uniq # -c with count number
