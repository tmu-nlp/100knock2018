import pymongo
import json

client = pymongo.MongoClient()
db = client.artists
co = db.my_collection


for line in open("artist.json", "r"):
	line_dic = json.loads(line)
	co.insert_one(line_dic)

# co.create_index([
# 	( "name", pymongo.ASCENDING ), 
# 	( "aliases.name", pymongo.ASCENDING ), 
# 	( "tags.value", pymongo.ASCENDING ), 
# 	( "rating.value", pymongo.ASCENDING )
# 	])

co.create_index([('name', pymongo.ASCENDING)])
co.create_index([('aliases.name', pymongo.ASCENDING)])
co.create_index([('tags.value', pymongo.ASCENDING)])
co.create_index([('rating.value', pymongo.ASCENDING)])