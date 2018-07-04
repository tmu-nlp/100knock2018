# pylint: disable=E1101
import leveldb
import gzip
import json


def make_db():
    db = leveldb.LevelDB('artists_DB_63')
    for line in gzip.open('artist.json.gz', 'rt', encoding='utf8'):
        artists = json.loads(line)
        if {'name', 'tags'} - set(artists):
            continue
        db.Put(artists['name'].encode('utf8'), json.dumps(artists['tags']).encode('utf8'))


def search_tags(name):
    'タグで検索し，結果を返す'
    db = leveldb.LevelDB('artists_DB_63')
    try:
        return json.loads(db.Get(name.encode('utf8')))
    except KeyError:
        return None


if __name__ == '__main__':
    make_db()
    while True:
        s = input('search:<name> quit:<Ctrl+C Return> -> ')
        tags = search_tags(s)
        if tags:
            print(f'The activity area of "{s}" tags:{", ".join(list(tag.values())[1:]) for tag in tags]}')
        else:
            print(f'Artist, "{s}" is not found.')


''' 問
63. オブジェクトを値に格納したKVS

KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）
のリストを検索するためのデータベースを構築せよ．
さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
'''

''' 実行結果
search:<name> quit:<Ctrl+C Return> -> BUMP OF CHICKEN
The activity area of "BUMP OF CHICKEN" tags:['japanese', 'rock', 'j-pop']
'''
