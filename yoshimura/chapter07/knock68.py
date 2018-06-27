'''
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
'''

from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client.database
collection = db.artist

results = collection.find({'tags.value': 'dance'})
results.sort('rating.count', pymongo.DESCENDING)

for doc in results[0:10]:
    print(f'{doc["name"]}({doc["rating"]["count"]})')
