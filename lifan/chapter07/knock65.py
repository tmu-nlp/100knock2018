import pymongo

client = pymongo.MongoClient()
db = client.artists
co = db.my_collection

for record in co.find({"name": "Queen"}):
	print(record)

# SHELL
# db.my_collection.find({name: "Queen"})