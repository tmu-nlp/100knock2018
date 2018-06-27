
def main():
    from knock64 import MusicDb

    db = MusicDb()
    tag = input("input tag: ").strip()
    query = {"tags.value": tag}
    pipeline = [
        {"$match": query},
        {"$group": {
            "_id": "$name", 
            "total": {"$sum": "$rating.count"}
            }
        },
        {"$sort": {"total": -1}},
        {"$limit": 10}
    ]

    artists = db.collection.aggregate(pipeline)

    for a in artists:
        print(a)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')