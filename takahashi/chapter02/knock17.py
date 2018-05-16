# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_table('../data/hightemp.txt', encoding="utf-8_sig", header=None)

items = df[0].unique()

print(items)
