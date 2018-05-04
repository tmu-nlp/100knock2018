# -*- coding: utf-8 -*-

import json
import gzip

filepath = "../data/jawiki-country.json.gz"
with gzip.open(filepath, 'rb') as f:
    for line in f:
        obj = json.loads(line.decode('utf-8'))
        if obj['title'] == 'イギリス':
            print(obj['text'])