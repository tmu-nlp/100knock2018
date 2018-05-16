# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_table('../data/hightemp.txt', encoding="utf-8_sig", header=None)
df = df.sort_values(by=2, ascending=True)

print(df)
