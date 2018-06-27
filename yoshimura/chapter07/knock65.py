'''
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
さらに，これと同様の処理を行うプログラムを実装せよ．
'''
from pymongo import MongoClient

client = MongoClient()
db = client.database
collection = db.artist

for doc in collection.find({'name': 'Queen'}):
    print(doc)


'''
インタラクティブシェルを用いた結果
> show dbs
admin     0.000GB
config    0.000GB
database  0.260GB
local     0.000GB
> use database
switched to db database
> show collections
artist
> db.artist.find({'name' : 'Queen'});
{ "_id" : ObjectId("5b2f46ddce45444bf1e42335"), "name" : "Queen", "area" : "Japan", "gender" : "Female", "tags" : [ { "count" : 1, "value" :"kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5b2f46dece45444bf1e4e9e1"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "month" : 6, "year" : 1970 }, "name" : "Queen", "area" : "United Kingdom", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5b2f46dfce45444bf1e6a439"), "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "id" : 992994, "name" : "Queen" }
{ "_id" : ObjectId("5b2f474ace45444cdd8a83b9"), "name" : "Queen", "area" : "Japan", "gender" : "Female", "tags" : [ { "count" : 1, "value" :"kamen rider w" }, { "count" : 1, "value" : "related-akb48" } ], "sort_name" : "Queen", "ended" : true, "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "type" : "Character", "id" : 701492, "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5b2f474bce45444cdd8b4a65"), "rating" : { "count" : 24, "value" : 92 }, "begin" : { "date" : 27, "month" : 6, "year" : 1970 }, "name" : "Queen", "area" : "United Kingdom", "tags" : [ { "count" : 2, "value" : "hard rock" }, { "count" : 1, "value" : "70s" }, { "count" : 1, "value" : "queen family" }, { "count" : 1, "value" : "90s" }, { "count" : 1, "value" : "80s" }, { "count" : 1, "value" : "glam rock" }, { "count" : 4, "value" : "british" }, { "count" : 1, "value" : "english" }, { "count" : 2, "value" : "uk" }, { "count" : 1, "value" : "pop/rock" }, { "count" : 1, "value" : "pop-rock" }, { "count" : 1, "value" : "britannique" }, { "count" : 1, "value" : "classic pop and rock" }, { "count" : 1, "value" : "queen" }, { "count" : 1, "value" : "united kingdom" }, { "count" : 1, "value" : "langham 1 studio bbc" }, { "count" : 1, "value" : "kind of magic" }, { "count" : 1, "value" : "band" }, { "count" : 6, "value" : "rock" }, { "count" : 1, "value" : "platinum" } ], "sort_name" : "Queen", "ended" : true, "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "type" : "Group", "id" : 192, "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5b2f474cce45444cdd8d04bd"), "ended" : true, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "id" : 992994, "name" : "Queen" }
'''

'''
プログラムの実行結果
{'_id': ObjectId('5b2f46ddce45444bf1e42335'), 'name': 'Queen', 'area': 'Japan', 'gender': 'Female', 'tags': [{'count': 1, 'value': 'kamen rider w'}, {'count': 1, 'value': 'related-akb48'}], 'sort_name': 'Queen', 'ended': True, 'gid': '420ca290-76c5-41af-999e-564d7c71f1a7', 'type':'Character', 'id': 701492, 'aliases': [{'name': 'Queen', 'sort_name': 'Queen'}]}
{'_id': ObjectId('5b2f46dece45444bf1e4e9e1'), 'rating': {'count': 24, 'value': 92}, 'begin': {'date': 27, 'month': 6, 'year': 1970}, 'name':'Queen', 'area': 'United Kingdom', 'tags': [{'count': 2, 'value': 'hard rock'}, {'count': 1, 'value': '70s'}, {'count': 1, 'value': 'queen family'}, {'count': 1, 'value': '90s'}, {'count': 1, 'value': '80s'}, {'count': 1, 'value': 'glam rock'}, {'count': 4, 'value': 'british'}, {'count': 1, 'value': 'english'}, {'count': 2, 'value': 'uk'}, {'count': 1, 'value': 'pop/rock'}, {'count': 1, 'value': 'pop-rock'}, {'count': 1, 'value': 'britannique'}, {'count': 1, 'value': 'classic pop and rock'}, {'count': 1, 'value': 'queen'}, {'count': 1, 'value': 'united kingdom'}, {'count': 1, 'value': 'langham 1 studio bbc'}, {'count': 1, 'value': 'kind of magic'}, {'count': 1, 'value': 'band'}, {'count': 6, 'value': 'rock'}, {'count': 1, 'value': 'platinum'}], 'sort_name': 'Queen', 'ended': True, 'gid': '0383dadf-2a4e-4d10-a46a-e9e041da8eb3', 'type': 'Group', 'id': 192, 'aliases': [{'name': '女王', 'sort_name': '女王'}]}
{'_id': ObjectId('5b2f46dfce45444bf1e6a439'), 'ended': True, 'gid': '5eecaf18-02ec-47af-a4f2-7831db373419', 'sort_name': 'Queen', 'id': 992994, 'name': 'Queen'}
{'_id': ObjectId('5b2f474ace45444cdd8a83b9'), 'name': 'Queen', 'area': 'Japan', 'gender': 'Female', 'tags': [{'count': 1, 'value': 'kamen rider w'}, {'count': 1, 'value': 'related-akb48'}], 'sort_name': 'Queen', 'ended': True, 'gid': '420ca290-76c5-41af-999e-564d7c71f1a7', 'type':'Character', 'id': 701492, 'aliases': [{'name': 'Queen', 'sort_name': 'Queen'}]}
{'_id': ObjectId('5b2f474bce45444cdd8b4a65'), 'rating': {'count': 24, 'value': 92}, 'begin': {'date': 27, 'month': 6, 'year': 1970}, 'name':'Queen', 'area': 'United Kingdom', 'tags': [{'count': 2, 'value': 'hard rock'}, {'count': 1, 'value': '70s'}, {'count': 1, 'value': 'queen family'}, {'count': 1, 'value': '90s'}, {'count': 1, 'value': '80s'}, {'count': 1, 'value': 'glam rock'}, {'count': 4, 'value': 'british'}, {'count': 1, 'value': 'english'}, {'count': 2, 'value': 'uk'}, {'count': 1, 'value': 'pop/rock'}, {'count': 1, 'value': 'pop-rock'}, {'count': 1, 'value': 'britannique'}, {'count': 1, 'value': 'classic pop and rock'}, {'count': 1, 'value': 'queen'}, {'count': 1, 'value': 'united kingdom'}, {'count': 1, 'value': 'langham 1 studio bbc'}, {'count': 1, 'value': 'kind of magic'}, {'count': 1, 'value': 'band'}, {'count': 6, 'value': 'rock'}, {'count': 1, 'value': 'platinum'}], 'sort_name': 'Queen', 'ended': True, 'gid': '0383dadf-2a4e-4d10-a46a-e9e041da8eb3', 'type': 'Group', 'id': 192, 'aliases': [{'name': '女王', 'sort_name': '女王'}]}
{'_id': ObjectId('5b2f474cce45444cdd8d04bd'), 'ended': True, 'gid': '5eecaf18-02ec-47af-a4f2-7831db373419', 'sort_name': 'Queen', 'id': 992994, 'name': 'Queen'}
'''