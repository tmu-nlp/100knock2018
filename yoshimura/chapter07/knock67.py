'''
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．
'''

from pymongo import MongoClient

client = MongoClient()
db = client.database
collection = db.artist

name = input('Please input artist name --> ')
for doc in collection.find({'aliases.name': f'{name}'}):
    print(doc)
