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
            break

ret = {}

lines = re.split(r'\n[\|\}]', txt)
for line in lines:
    r = re.compile(r'\'{5}|\'{3}|\'{2}')
    if r.search(line) is not None:
        line = r.sub('', line)
    target = re.split(r'\s=\s', line)
    if len(target) == 2:

        ret[target[0]] = target[1]

for key in ret.keys():
    print(key, ret[key])