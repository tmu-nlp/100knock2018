#!/usr/bin/env bash

# without cat the columns
# t for field delim, k for key/field
cat hightemp.txt | sort -t $'\t' -k 3 -r
