from knock64 import MusicDb

db = MusicDb()
name = input("input artist name: ").strip()
for ret in db.collection.find({"name": name}):
    print(ret)
