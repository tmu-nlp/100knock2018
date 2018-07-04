# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pymongo
import json

client = MongoClient()
db = client.knock64_db
db.drop_collection('knock64_collection')
collection = db.knock64_collection

block = []
for i, line in enumerate(open('artist.json', 'r')):
    artisit_dic = json.loads(line)
    block.append(artisit_dic)
    if i % 5000 == 0 and i != 0:
        collection.insert_many(block)
        block = []
collection.insert_many(block)

collection.create_index([('name', pymongo.ASCENDING)])
collection.create_index([('aliases.name', pymongo.ASCENDING)])
collection.create_index([('tags.value', pymongo.ASCENDING)])
collection.create_index([('rating.value', pymongo.ASCENDING)])
