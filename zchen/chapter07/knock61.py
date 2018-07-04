from knock60 import open_db
from sys import argv
# for chaining serveral iterators into one, tosho-san was using it as a guard
from itertools import chain

# find exact key by filtering, then find their values
def query_music(r, mode, artist, value_query=None):
    if mode not in ('area', 'tag'):
        raise Exception

    key = '%s:%s' % (mode.upper(), artist)
    names = []

    # keys & scan:
    # https://stackoverflow.com/questions/22255589/get-all-keys-in-redis-database-with-python
    for i, real_key in enumerate(chain(r.scan(key), [None])):
        if real_key == None or i % 10000 == 0:
            values = query_value_pipe(r, mode, names)
            for k, v in zip(names, values):
                if value_query == None or value_query == v:
                    if mode == 'area':
                        yield k[5:], v
                    elif mode == 'tag':
                        tags = {
                            tk.decode('utf-8'):int(tv.decode('utf-8')) for tk, tv in v.items()
                        }
                        yield k[4:], tags
            names = []
        if real_key != None:
            names.append(name.decode('utf-8'))

def query_value_pipe(r, mode, keys=[]):
    pipe = r.pipeline()
    for key in keys:
        if mode == 'area':
            pipe.get(key) # an artist has ccts in many areas
        if mode == 'tag':
            pipe.hgetall(key) # has more tags with information
    values = pipe.execute()

    if mode == 'area':
        values = [v.decode('utf-8') for v in values]
    return values

if __name__ == '__main__':
    artist = input("input artist name: ").strip()
    with open_db() as r:
        for artist, area in query_music(r, 'area', artist):
            print(f'{artist}: {area}')
