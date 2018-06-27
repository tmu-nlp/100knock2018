# mongoDB shell
# >  mongo
# >> use MusicBrainz
# >> db.artist.fined({'name':'Queen')



import pymongo
import pprint



def print_Queen(collection, data_out):
    for part_queen in collection.find({'name':'Queen'}):
        pprint.pprint(part_queen, data_out)


if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist
    with open('result/knock65_result.txt', 'w') as data_out:
        print_Queen(collection, data_out)
