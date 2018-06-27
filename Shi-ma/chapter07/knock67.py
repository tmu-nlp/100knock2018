import pymongo
import sys
import pprint



if __name__ == '__main__':
    name_aliases = str(sys.argv[1])
    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist
    if collection.find({'aliases.name':name_aliases}).count() != 0:
        for part_aliases in collection.find({'aliases.name':name_aliases}):
            pprint.pprint(part_aliases)
    else:
        print('Not found.')
