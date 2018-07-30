import pymongo

def count(area):
    client = pymongo.MongoClient()
    db = client.db_knock64
    collection = db.collection_knock64

    count = collection.count({'area': area})
    return count

if __name__ == '__main__':
    print(count('Japan'))


''' 問
66. 検索件数の取得

MongoDBのインタラクティブシェルを用いて，
活動場所が「Japan」となっているアーティスト数を求めよ．
'''

''' 実行結果
mongo db_knock64
> db.collection_knock64.count({"area":"Japan"})
22742
'''
