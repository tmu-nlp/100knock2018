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

# categories = re.findall('^[=]{2}.*[=]{2}$', txt, re.MULTILINE)
# print(categories)

categories = re.findall('^\[\[Category:.*\]\]$', txt, re.MULTILINE)
print(categories)