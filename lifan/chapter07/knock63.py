import redis
import json
import pickle
import sys

db = redis.StrictRedis(host='localhost', port=6379, db=1)

if len(db.keys()) == 0:
	artist_dic = {}
	for line in open("artist.json", "r"):
		line_dic = json.loads(line)
		if 'name' in line_dic and 'tags' in line_dic:
			artist_dic[line_dic["name"]] = pickle.dumps(line_dic["tags"])

	db.mset(artist_dic)

try:
	tags = pickle.loads(db.get(sys.argv[1]))
	print(tags)
except:
	print("No tags!")
