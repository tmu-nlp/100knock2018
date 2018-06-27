# pylint: disable=E1101
import leveldb
import gzip
import json


def save_db():
    db = leveldb.LevelDB('artists_DB')
    for line in gzip.open('artist.json.gz', 'rt', encoding='utf8'):
        artists = json.loads(line)
        if {'name', 'area'} - set(artists):
            continue
        db.Put(artists['name'].encode('utf8'), artists['area'].encode('utf8'))

if __name__ == '__main__':
    save_db()


''' 問
60. KVSの構築

Key-Value-Store (KVS) を用い，
アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
'''

''' 実行結果

'''
