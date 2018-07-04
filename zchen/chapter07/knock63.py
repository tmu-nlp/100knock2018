from knock60 import open_db
from knock61 import query_music
from sys import argv
import itertools

if __name__ == '__main__':
    artist = input("input artist name: ").strip()
    with open_db() as r:
        for artist, tags in query_music(r, 'tag', artist):
            print(f'{artist}: {len(tags)} tags')
            for tag, count in tags.items():
                print(f'\t{tag}: {count}')
