#!/usr/bin/env bash
cut -f 1 < '../data/hightemp.txt' | sort | uniq -c | sort -k1,1 -r