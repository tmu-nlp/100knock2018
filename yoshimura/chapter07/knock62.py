'''
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
'''
import leveldb

db = leveldb.LevelDB('db')
num = len([data[0] for data in db.RangeIter() if data[1] == 'Japan'.encode()])
print(f'{num}件')
