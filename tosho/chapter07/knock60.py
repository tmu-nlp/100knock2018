'''
docker run --name redis -d -p 6379:6379 redis redis-server --appendonly yes
docker rm redis -f
'''

import redis
import os
import urllib.request
import json, gzip
import itertools
from sys import argv

class Music:
    def __init__(self, name, area):
        self.name = name
        self.area = area

def main():
    r = init_kvs(len(argv)>1 and argv[1]=='flushdb')
    print(f'{len(r.keys())} items')

def init_kvs(flushdb=False):
    r = redis.Redis(host='localhost', port=6379, db=0)
    if flushdb or len(r.keys()) == 0:
        r.flushdb()

        pipe = r.pipeline()
        for i, music in enumerate(load_music_brainz()):
            pipe.set(music.name, music.area)
            if i % 10000 == 0:
                pipe.execute()
                pipe = r.pipeline()
        pipe.execute()
    return r

def load_music_brainz():
    download_url = 'http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz'
    file_name = 'artist.json.gz'

    if os.path.exists(file_name) is False:
        urllib.request.urlretrieve(download_url, file_name)

    lines = sum(1 for line in gzip.open(file_name, 'r'))
    with gzip.open(file_name, 'r') as f:
        for i, line in enumerate(f):
            data = json.loads(line)
            if i % 10000 == 0:
                print(f'{i} / {lines} items')
            if 'name' in data and 'area' in data:
                yield Music(data['name'], data['area'])

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')