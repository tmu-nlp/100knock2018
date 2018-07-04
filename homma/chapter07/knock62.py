# pylint: disable=E1101
import leveldb


def main():
    db = leveldb.LevelDB('artists_DB')
    return sum(1 for _, area in db.RangeIter() if area == b'Japan')

if __name__ == '__main__':
    print(main())


''' 問
62. KVS内の反復処理

60で構築したデータベースを用い，
活動場所が「Japan」となっているアーティスト数を求めよ．
'''

''' 実行結果
22119
'''
