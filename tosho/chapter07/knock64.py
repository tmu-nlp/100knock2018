'''
start MongoDB via Docker:
docker run --name mongo -d -p 27017:27017 mongo

reference:
https://qiita.com/ognek/items/a37dd1cd0e26e6adecaa
'''
from pymongo import MongoClient, IndexModel
import os, gzip, json, urllib, sys
from itertools import chain
import datetime, uuid

class Music:
    def __init__(self, id, 
            gid=None, name=None, sort_name=None, area=None, aliases={}, 
            begin=None, end=None, tags={}, rating=None
        ):
        self.id = id
        self.gid = gid
        self.name = name
        self.sort_name = sort_name
        self.area = area
        self.aliases = aliases
        self.begin = begin
        self.end = end
        self.tags = tags
        self.rating = rating

class MusicDb:
    def __init__(self, host='localhost', port=27017, db_name='chapter07'):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.mongo = MongoClient(self.host, self.port)
        self.db = self.mongo.get_database(name=self.db_name)
        self.collection = self.db.get_collection('artists')

    def flush_db(self):
        print('Droping all contents... ', end='', flush=True)
        self.db.drop_collection(self.collection)
        self.collection = self.db.get_collection('artists')
        print('Done')

        print('Adding index... ', end='', flush=True)
        self.collection.create_index('name')
        self.collection.create_index('aliases.name')
        self.collection.create_index('tags.value')
        self.collection.create_index('rating.value')
        print('Done')

    def insert_artist(self, artist_dict):
        if len(artist_dict) > 0:
            for obj in artist_dict:
                self.conv_dot(obj)
            result = self.collection.insert_many(artist_dict)
            return result
        else:
            return None

    def conv_dot(self, obj):
        '''
        http://iga-ninja.hatenablog.com/entry/2016/07/10/153818
        '''
        if isinstance(obj, dict):
            for org_key in obj.keys():
                new_key = org_key
                if '.' in org_key:
                    new_key = org_key.translate({ord("."): ord("_")})
                    obj[new_key] = obj.pop(org_key)

                self.conv_dot(obj[new_key])

        elif isinstance(obj, list):
            for val in obj:
                self.conv_dot(val)
        else:
            pass

    def artists_count(self):
        return self.collection.count()

def main():
    flushdb = len(sys.argv) > 1 and sys.argv[1] == 'flushdb'

    db = MusicDb()

    if flushdb:
        deleting = db.artists_count()
        db.flush_db()
        deleted = db.artists_count()
        print(f'{deleting} items deleted. Now collection has {deleted} items.')

    block = []
    batch_size = 50000
    for i, data in enumerate(chain(load_music_brainz(), [None])):
        if data == None or i % batch_size == 0:
            db.insert_artist(block)
            block = []
        if data != None:
            block.append(data)

    print(f'{db.artists_count()} artists')
        
def parse_one_music(data):
    attr = {}
    attr['id'] = data['id']
    attr['gid'] = data['gid'] if 'gid' in data else None
    attr['name'] = data['name'] if 'name' in data else None
    attr['sort_name'] = data['sort_name'] if 'sort_name' in data else None
    attr['area'] = data['area'] if 'area' in data else None
    if 'aliases' in data:
        attr['aliases'] = {}
        for an, asn in data['aliases']:
            attr['aliases'][an] = asn
    if 'begin' in data:
        date = map(str, data['begin'].values())
        attr['begin'] = '/'.join(date)
    if 'end' in data:
        date = map(str, data['end'].values())
        attr['end'] = '/'.join(date)
    if 'tags' in data:
        attr['tags'] = {}
        for tv, tc in [(tag['value'], tag['count']) for tag in data['tags']]:
            attr['tags'][tv] = int(tc)
    if 'rating' in data:
        attr['rating'] = data['rating']
    
    return attr

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
            yield data


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')