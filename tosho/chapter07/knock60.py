'''
docker run --name redis -d -p 6379:6379 redis redis-server --appendonly yes
docker rm redis -f
'''

import redis
import os
import urllib.request
import json, gzip
import itertools

class Music:
    def __init__(self, name, area):
        self.name = name
        self.area = area

def main():
    r = init_kvs()
    print(f'{len(r.keys())} items')

def init_kvs():
    r = redis.Redis(host='localhost', port=6379, db=0)
    if len(r.keys()) == 0:
        for music in load_music_brainz():
            r.set(music.name, music.area)
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