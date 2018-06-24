from knock60 import init_kvs, Music
from sys import argv

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

def query_music(r, query):
    for name in r.keys(pattern=query):
        yield Music(name, r.get(name))

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')