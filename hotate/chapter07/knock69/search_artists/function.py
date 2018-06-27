# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json


def search_artist(name, limit):
    client = MongoClient()
    db = client.knock64_db
    collection = db.knock64_collection

    for post in collection.find({"name": name}).sort([("rating.count", -1)]).limit(limit):
        yield post


def search_area(area, limit):
    client = MongoClient()
    db = client.knock64_db
    collection = db.knock64_collection

    for post in collection.find({"area": area}).sort([("rating.count", -1)]).limit(limit):
        yield post


def search_aliases_name(name, limit):
    client = MongoClient()
    db = client.knock64_db
    collection = db.knock64_collection

    for post in collection.find({"aliases.name": name}).sort([("rating.count", -1)]).limit(limit):
        yield post


def search_tag(tag, limit):
    client = MongoClient()
    db = client.knock64_db
    collection = db.knock64_collection

    for rank in collection.find({"tags.value": tag}).sort([("rating.count", -1)]).limit(limit):
        yield rank


