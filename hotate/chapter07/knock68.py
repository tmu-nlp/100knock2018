# -*- coding: utf-8 -*-
from pymongo import MongoClient


def search_dance_rank():
    client = MongoClient()
    db = client.knock64_db
    collection = db.knock64_collection

    for rank in collection.find({"tags.value": "dance"}).sort([("rating.count", -1)]).limit(10):
        yield rank


if __name__ == '__main__':
    for rank in search_dance_rank():
        print(rank)
