# -*- coding: utf-8 -*-

import json
import gzip
import re

filepath = "../data/jawiki-country.json.gz"
txt = ''

with gzip.open(filepath, 'rb') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj['title'] == 'イギリス':
            txt = obj['text']
            # print(txt)

for item in re.finditer(r'()File:(.*?)\|', txt, re.MULTILINE):
    print(item.group().split(':')[1].replace('|', ''))
for item in re.finditer(r'ファイル:(.*?)\|', txt, re.MULTILINE):
    print(item.group().split(':')[1].replace('|', ''))