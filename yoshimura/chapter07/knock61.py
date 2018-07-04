'''
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
'''
import leveldb

db = leveldb.LevelDB('db')
name = input('Please input artist name -> ')
area = db.Get(name.encode())
print('area: ' + area.decode())
