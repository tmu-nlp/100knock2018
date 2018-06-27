import pymongo



if __name__ == '__main__':
    client = pymongo.MongoClient()
    db = client.MusicBrainz
    collection = db.artist
    for i in collection.find({'$and':[{'tags.value':'dance'}, {'rating.count':{'$exists':True}}]}).sort('rating.count', -1).limit(10):
        print(i['name'] + '\t' + str(i['rating']['count']))
