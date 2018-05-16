# -*- coding: utf-8 -*-

import json
'''
import gzip

file_name = "jawiki-country.json.gz"
with gzip.open(file_name, "rb") as f:
    d = f.read()
    with open(file_name[:-3], "wb") as jsonfile:#gzを消す
        jsonfile.write(d)
'''


def extraction(title):
    with open('jawiki-country.json', 'r') as f:
        for line in f:
            json_file = json.loads(line)
            if title in json_file["title"]:
                return json_file["text"]
    return ''


if __name__ == '__main__':
    print(extraction('イギリス'))
