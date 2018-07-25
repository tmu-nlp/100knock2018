from knock64 import MusicDb

db = MusicDb()
name = input("input artist name: ").strip()
found = db.collection.find({"area": name}).count()
print(f'{found} artists found')
