import redis
import sys

db = redis.StrictRedis(host='localhost', port=6379, db=0)

print(db.get(sys.argv[1]).decode())