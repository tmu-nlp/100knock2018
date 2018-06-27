import json
import gzip
import pymongo



def make_artist_DB(data_js_path, collection):
    collection.drop()  # DBの初期化が必要 #
    with gzip.open(data_js_path, 'r') as data_js:
        temp = []
        for i, line in enumerate(data_js):
            data_dict = json.loads(line.decode('utf-8'))
            temp.append(data_dict)
            if (i + 1) % 10**4 == 0:
                print('{} items were registered'.format(i + 1))
                collection.insert_many(temp)
                temp = []
        if temp != []:
            print('{} items were registered'.format(i + 1))
            collection.insert_many(temp)


def make_artist_INDEX(collection):
    keys_index = ['name', 'aliases.name', 'tags.value', 'rating.value']
    for key_index in keys_index:
        collection.create_index([(key_index, pymongo.ASCENDING)])


if __name__ == '__main__':
    data_js_path = '../data/artist.json.gz'
    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist
    make_artist_DB(data_js_path, collection)
    make_artist_INDEX(collection)
