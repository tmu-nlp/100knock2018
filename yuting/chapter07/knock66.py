from pymongo import MongoClient


def search_japan_count():
    client = MongoClient()
    db = client.knock64_db
    collection = db.knock64_collection

    count = collection.find({"area": "Japan"}).count()
    return count


if __name__ == '__main__':
    print(search_japan_count())