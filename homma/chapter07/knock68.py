import pymongo


def main():
    client = pymongo.MongoClient()
    db = client.db_knock64
    collection = db.collection_knock64

    for record in collection.find({'tags.value': 'dance'}).sort([('rating.count', -1)]).limit(10):
        yield f"{record['name']}\t{record['rating']['count']}"


if __name__ == '__main__':
    for info in main():
        print(info)


''' 問
68. ソート
"dance"というタグを付与されたアーティストの中で
レーティングの投票数が多いアーティスト・トップ10を求めよ．
'''

''' 実行結果
Madonna 26
Björk   23
The Prodigy     23
Rihanna 15
Britney Spears  13
Maroon 5        11
Adam Lambert    7
Fatboy Slim     7
Basement Jaxx   6
Cornershop      5
'''
