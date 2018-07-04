# pylint: disable=E1101
import leveldb


def search_kvs(name):
    '''
    アーティスト名から そのアーティストの活動場所 を返す  
    その名前のアーティストがいなければ None を返す
    '''
    db = leveldb.LevelDB('db_knock60')
    try:
        area = db.Get(name.encode('utf8')).decode('utf8')
    except KeyError:
        area = None
    return area

if __name__ == '__main__':
    while True:
        s = input('search:<name> quit:<Ctrl+C Return> -> ')
        area = search_kvs(s)
        if area:
            print(f'The activity area of "{s}" area:{area}')
        else:
            print(f'Artist, "{s}" is not found.')


''' 問
61. KVSの検索

60で構築したデータベースを用い，
特定の（指定された）アーティストの活動場所を取得せよ．
'''

''' 実行結果
search:<name> quit:<Ctrl+C Return> -> 123
The activity area of "123" area:Turkey
search:<name> quit:<Ctrl+C Return> -> 1
The activity area of "1" area:United States
search:<name> quit:<Ctrl+C Return> -> a
Artist, "a" is not found.
'''
