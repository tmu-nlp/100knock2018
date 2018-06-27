import pymongo
import sys

client = pymongo.MongoClient()
db = client.artists
co = db.my_collection

for record in co.find({"aliases.name": sys.argv[1]}):
	print(record)