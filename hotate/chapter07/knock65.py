# -*- coding: utf-8 -*-
from pymongo import MongoClient


def search_artist(name):
    client = MongoClient()
    db = client.knock64_db
    collection = db.knock64_collection

    for post in collection.find({"name": name}):
        yield post


if __name__ == '__main__':
    while True:
        input_ = input()
        if input_ == 'quit':
            break
        else:
            for info in search_artist(input_):
                print(info)

# use knock64_db
# db.knock64_collection.find({"name":"Queen"})
