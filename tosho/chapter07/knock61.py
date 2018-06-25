from knock60 import init_kvs, Music
from sys import argv
from itertools import chain

def main():

    r = init_kvs()
    if len(argv) > 1:
        query = f'*{argv[1]}*'
        c = 0
        for music in query_music(r, query):
            print(f'{music.name}: {music.area}')
            c += 1

        print('='*50)
        print(f'{c} items')

def query_music(r, key_query='*', value_query=None):
    names = []
    for i, name in enumerate(chain(r.keys(pattern=key_query), [None])):
        if name == None or i % 10000 == 0:
            values = query_value_pipe(r, names)
            for k, v in zip(names, values):
                if value_query == None or value_query == v:
                    yield Music(k, v)
            names = []
        if name != None:
            names.append(name.decode('utf-8'))

def query_value_pipe(r, keys=[]):
    values = []
    pipe = r.pipeline()
    for key in keys:
        pipe.get(key)
    values = pipe.execute()
    for i, v in enumerate(values):
        values[i] = v.decode('utf-8')
    return values  

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')