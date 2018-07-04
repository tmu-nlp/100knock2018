import gzip
import json
import redis
# 参考
# http://www.denzow.me/entry/2017/10/07/233233

def open_db(refresh = False):
    pool = redis.ConnectionPool(host = '127.0.0.1', port = 7777, db = 0)
    r = redis.StrictRedis(connection_pool = pool)
    if refresh: r.flushdb()
    return r

def get_data(fname = "artist.json.gz"):
    with gzip.open(fname) as fr:
        for line in fr:
            line = json.loads(line)
            if 'name' in line and 'area' in line:
                yield line # encode to tranlate ascii into utf8 | decode into b

def make_db(package_size = 5000):
    with open_db(refresh = True) as r:
        pipe = r.pipeline()
        for i, item in enumerate(get_data()):
            pipe.set('AREA:' + item['name'], item.get('area', ''))
            if 'tags' in item:
                tags = {tag['value']:int(tag['count']) for tag in item['tags']}
                pipe.hmset('TAG:' + item['name'], tags)
            if i and i % package_size == 0:
                pipe.execute()
                pipe = r.pipeline()
        pipe.execute()
            # gather and transfer between server and clients
            # collections slice
            # hash all
            # cProfile mongodb grammar philosopy

#def check_db():
#    with open_db() as r:
#    print(r.lrange('ch06', 0 , 10))

if __name__ == '__main__':
    make_db()
    #check_db()
