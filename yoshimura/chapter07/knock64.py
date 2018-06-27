'''
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ:
name, aliases.name, tags.value, rating.value
'''
from pymongo import MongoClient
import pymongo
import gzip
import json

unit = 100000  # コレクションにinsertする単位

# MongoDBのデータベースdbのコレクションartistにアクセス
client = MongoClient()  # MongoClient作成
db = client.database  # データベース取得
collection = db.artist  # コレクション取得

with gzip.open('artist.json.gz', 'r') as data_file:
    buf = []
    for i, line in enumerate(data_file, 1):
        json_dict = json.loads(line)
        buf.append(json_dict)
        if i % unit == 0:
            collection.insert_many(buf)
            buf = []
            print(f'{i} finished')
    collection.insert_many(buf)
    print(f'{i} finished')


# インデックス作成
collection.create_index([("name", pymongo.ASCENDING)])
collection.create_index([("aliases.name", pymongo.ASCENDING)])
collection.create_index([("tags.value", pymongo.ASCENDING)])
collection.create_index([("rating.value", pymongo.ASCENDING)])
