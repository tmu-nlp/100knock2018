'''
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
'''
import gzip
import json
import leveldb

db = leveldb.LevelDB('db')

with gzip.open('artist.json.gz', 'r') as data_file:
    for line in data_file:
        json_dict = json.loads(line)
        name = json_dict['name']
        area = json_dict['area'] if 'area' in json_dict else ''
        db.Put(name.encode(), area.encode())
