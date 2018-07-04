'''
66. 検索件数の取得
MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ．
'''

'''
> show dbs
admin     0.000GB
config    0.000GB
database  0.135GB
local     0.000GB
> use database
switched to db database
> show collections
artist
> db.artist.find({'area': 'Japan'}).count()
22821
'''
