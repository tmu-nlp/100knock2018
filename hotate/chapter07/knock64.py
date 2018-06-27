# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pymongo
import json

client = MongoClient()
db = client.knock64_db
collection = db.knock64_collection

for line in open('artist.json', 'r'):
    artisit_dic = json.loads(line)
    collection.insert_one(artisit_dic)

collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
