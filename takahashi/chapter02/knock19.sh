#!/usr/bin/env bash
cut -f 1 < 'test19.txt' | sort | uniq -c | sort -k1,1 -r