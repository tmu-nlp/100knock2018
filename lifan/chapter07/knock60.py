import redis
import json

db = redis.StrictRedis()

artist_dic = {}
for line in open("artist.json", "r"):
	line_dic = json.loads(line)
	if 'name' in line_dic and 'area' in line_dic:
		artist_dic[line_dic["name"]] = line_dic["area"]

db.mset(artist_dic)

