from knock60 import init_kvs, Music
from knock61 import query_music
from sys import argv
import itertools

def main():
    artist = input("input artist name: ").strip()
    r = init_kvs()
    for music in query_music(r, 'tag', artist):
        print(f'{music.name}: {len(music.tags)} tags')
        for tag, count in music.tags.items():
            print(f'\t{tag}: {count}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')