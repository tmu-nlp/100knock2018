# coding: utf-8
import gzip
import json
import sys

with gzip.open('jawiki-country.json.gz', 'rt', encoding='utf-8') as data_file:
    for line in data_file:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            print(json_dict['text'])
            with open('Briten.txt', 'w', encoding='utf-8') as result:
                result.write(json_dict['text'])
            break

            

        