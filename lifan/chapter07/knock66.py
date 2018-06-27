import pymongo

client = pymongo.MongoClient()
db = client.artists
co = db.my_collection

print(co.find({"area": "Japan"}).count())

# SHELL
# db.my_collection.find({area: "Japan"}).count()
# 22821