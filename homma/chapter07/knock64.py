import gzip
import json
import pymongo
from tqdm import tqdm as tq


def main():
    client = pymongo.MongoClient()
    db = client.db_knock64
    collection = db.collection_knock64

    batch = []
    for i, line in tq(enumerate(gzip.open('artist.json.gz', 'rt', encoding='utf8'))):
        jdata = json.loads(line)
        batch.append(jdata)
        if not i % 10000 and batch:
            collection.insert_many(batch)
            batch = []

    collection.create_index([('name', pymongo.ASCENDING)])
    collection.create_index([('aliases.name', pymongo.ASCENDING)])
    collection.create_index([('tags.value', pymongo.ASCENDING)])
    collection.create_index([('rating.value', pymongo.ASCENDING)])


if __name__ == '__main__':
    main()


''' 問
64. MongoDBの構築

アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ:
    name, aliases.name, tags.value, rating.value
'''

''' 実行結果
http://kageura.hatenadiary.jp/entry/2018/01/09/Windows%E7%89%88MongoDB%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%83%BBMongoShell%E3%82%92%E9%80%9A%E3%81%97%E3%81%A6CRUD%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%82%92%E6%89%93
とかを参考に MongoDB をインストールし，データ格納用ディレクトリを作成し，起動しておく
'''
