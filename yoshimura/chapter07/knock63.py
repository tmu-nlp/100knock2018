'''
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
'''
import json
import gzip
import leveldb

try:
    db = leveldb.LevelDB('db2', error_if_exitst=True)  # 存在したらエラー

    with gzip.open('artist.json.gz', 'r') as data_file:
        for line in data_file:
            json_dict = json.loads(line)
            name = json_dict['name']
            tag_list = json_dict['tags'] if 'tags' in json_dict else []

            db.Put(name.encode(), json.dumps(tag_list).encode())
except:
    db = leveldb.LevelDB('db2')


name = input('Please input artist name -> ')
tag_list = json.loads(db.Get(name.encode()).decode())
for tag_dict in tag_list:
    print(f'{tag_dict["value"]}({tag_dict["count"]})')
