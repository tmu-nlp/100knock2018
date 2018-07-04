# mongoDB shell
# >  mongo
# >> use MusicBrainz
# >> db.artist.fined({'area':'Japan')



import pymongo



if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist
    print(collection.find({'area':'Japan'}).count())
