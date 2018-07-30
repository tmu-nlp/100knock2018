# pylint: disable=E1101
import pymongo
import gzip
import json


def search_artist(name):
    client = pymongo.MongoClient()
    db = client.db_knock64
    collection = db.collection_knock64

    for record in collection.find({'name': name}):
        yield record

if __name__ == '__main__':
    while True:
        s = input('search:<name> quit:<Ctrl+C Return> -> ')
        for info in search_artist(s):
            print(info)


''' 問
65. MongoDBの検索

MongoDBのインタラクティブシェルを用いて，
"Queen"というアーティストに関する情報を取得せよ．
さらに，これと同様の処理を行うプログラムを実装せよ．
'''

''' 実行結果
mongo を起動しておく

search:<name> quit:<Ctrl+C Return> -> Queen
{'_id': ObjectId('5b5ef95865c91425e4f89494'), 'name': 'Queen', 'area': 'Japan', 'gender': 'Female', 'tags': [{'count': 1, 'value': 'kamen rider w'}, {'count': 1, 'value': 'related-akb48'}], 'sort_name': 'Queen', 'ended': True, 'gid': '420ca290-76c5-41af-999e-564d7c71f1a7', 'type': 'Character', 'id': 701492, 'aliases': [{'name': 'Queen', 'sort_name': 'Queen'}]}
{'_id': ObjectId('5b5ef95a65c91425e4f95b40'), 'rating': {'count': 24, 'value': 92}, 'begin': {'date': 27, 'month': 6, 'year': 1970}, 'name': 'Queen', 'area': 'United Kingdom', 'tags': [{'count': 2, 'value': 'hard rock'}, {'count': 1, 'value': '70s'}, {'count': 1, 'value': 'queen family'}, {'count': 1, 'value': '90s'}, {'count': 1, 'value': '80s'}, {'count': 1, 'value': 'glam rock'}, {'count': 4, 'value': 'british'}, {'count': 1, 'value': 'english'}, {'count': 2, 'value': 'uk'}, {'count': 1, 'value': 'pop/rock'}, {'count': 1, 'value': 'pop-rock'}, {'count': 1, 'value': 'britannique'}, {'count': 1, 'value': 'classic pop and rock'}, {'count': 1, 'value': 'queen'}, {'count': 1, 'value': 'united kingdom'}, {'count': 1, 'value': 'langham 1 studio bbc'}, {'count': 1, 'value': 'kind of magic'}, {'count': 1, 'value': 'band'}, {'count': 6, 'value': 'rock'}, {'count': 1, 'value': 'platinum'}], 'sort_name': 'Queen', 'ended': True, 'gid': '0383dadf-2a4e-4d10-a46a-e9e041da8eb3',
'type': 'Group', 'id': 192, 'aliases': [{'name': '女王', 'sort_name': '女王'}]}
{'_id': ObjectId('5b5ef95e65c91425e4fb1598'), 'ended': True, 'gid': '5eecaf18-02ec-47af-a4f2-7831db373419', 'sort_name': 'Queen', 'id': 992994, 'name': 'Queen'}
'''
