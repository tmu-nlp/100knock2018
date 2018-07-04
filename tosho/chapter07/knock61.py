from knock60 import init_kvs, Music
from sys import argv
from itertools import chain

def main():
    artist = input("input artist name: ").strip()
    r = init_kvs()

    for music in query_music(r, 'area', artist):
        print(f'{music.name}: {music.area}')

def query_music(r, mode, artist, value_query=None):
    names = []

    key_query = artist
    if mode == 'area':
        key_query = 'AREA:' + artist
    elif mode == 'tag':
        key_query = 'TAG:' + artist

    for i, name in enumerate(chain(r.keys(pattern=key_query), [None])):
        if name == None or i % 10000 == 0:
            values = query_value_pipe(r, mode, names)
            for k, v in zip(names, values):
                if value_query == None or value_query == v:
                    if mode == 'area':
                        yield Music(k[5:], v)
                    elif mode == 'tag':
                        m = Music(k[4:], None)
                        for tk, tv in v.items():
                            m.tags[tk.decode('utf-8')] = int(tv.decode('utf-8'))
                        yield m
            names = []
        if name != None:
            names.append(name.decode('utf-8'))

def query_value_pipe(r, mode, keys=[]):
    values = []
    pipe = r.pipeline()
    for key in keys:
        if mode == 'area':
            pipe.get(key)
        if mode == 'tag':
            pipe.hgetall(key)
    values = pipe.execute()

    if mode == 'area':
        for i, v in enumerate(values):
            values[i] = v.decode('utf-8')
    return values  

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')