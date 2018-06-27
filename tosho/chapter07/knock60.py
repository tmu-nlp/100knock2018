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
    def __init__(self, name, area=''):
        self.name = name
        self.area = area
        self.tags = {}

def main():
    r = init_kvs(len(argv)>1 and argv[1]=='flushdb')
    print(f'{len(r.keys())} items')

def init_kvs(flushdb=False):
    r = redis.Redis(host='localhost', port=6379, db=0)
    if flushdb or len(r.keys()) == 0:
        r.flushdb()
        pipe = r.pipeline()
        for i, music in enumerate(load_music_brainz()):
            # AREA
            pipe.set('AREA:' + music.name, music.area)
            # TAG
            if len(music.tags) > 0:
                pipe.hmset('TAG:' + music.name, music.tags)
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
            if 'name' in data:
                name = data['name']
                area = data['area'] if 'area' in data else ''
                music = Music(name, area)
                if 'tags' in data:
                    for tag in data['tags']:
                        music.tags[tag['value']] = int(tag['count'])
                yield music

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')