# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_table('../data/hightemp.txt', encoding="utf-8_sig", header=None)

# items = df[0].unique() # introduced by takahashi
# df = df.sort_values(by=2, ascending=True) # introduced by takahashi
print(df[0].value_counts()) # introduced by takahashi

# line is the unit for sort by default
# unique/set will never be made without sort
# check more by examples in that book
# cut -d $'\t' -f 1 "hightemp.txt" | sort | uniq -c | sort -k 1 -r
