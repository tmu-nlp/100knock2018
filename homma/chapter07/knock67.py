import pymongo


def main(name):
    client = pymongo.MongoClient()
    db = client.db_knock64
    collection = db.collection_knock64

    for record in collection.find({'aliases.name': name}):
        yield record

if __name__ == '__main__':
    while True:
        s = input('search:<name> quit:<Ctrl+C Return> -> ')
        for info in main(s):
            print(info)


''' 問
67. 複数のドキュメントの取得

特定の（指定した）別名を持つアーティストを検索せよ．
'''

''' 実行結果
search:<name> quit:<Ctrl+C Return> -> バンプ・オブ・チキン
{'_id': ObjectId('5b5ef95365c91425e4f67bcd'), 'begin': {'year': 1994}, 'name': 'BUMP OF CHICKEN', 'area': 'Japan', 'tags': [{'count': 1, 'value': 'japanese'}, {'count': 1, 'value': 'rock'}, {'count': 1, 'value': 'j-pop'}], 'sort_name': 'BUMP OF CHICKEN', 'ended': True, 'gid': '0f718079-e5ea-4cfb-b512-b2d04da66901', 'type': 'Group', 'id': 122757, 'aliases': [{'name': 'Bump of Chiken', 'sort_name': 'Bump of Chiken'}, {'name': 'バンプ・オブ・チキン', 'sort_name': 'バンプ・オブ・チキン'}]}
'''
