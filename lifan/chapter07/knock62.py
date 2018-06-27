import redis
import sys

db = redis.StrictRedis(host='localhost', port=6379, db=0)

count = 0
for key in db.keys():
	if db.get(key).decode() == "Japan":
		count += 1

print(count)