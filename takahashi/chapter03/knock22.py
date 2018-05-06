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

# for item in re.finditer(r'^[=]{2}.*[=]{2}$', txt, re.MULTILINE):
#     print(item.group().replace("=", ""))

for item in re.finditer(r'^\[\[Category:.*\]\]$', txt, re.MULTILINE):
    print(item.group().replace("[[Category:", "").replace("]", ""))
