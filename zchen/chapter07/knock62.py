from knock60 import open_db
from knock61 import query_music
from sys import argv
import itertools

if __name__ == '__main__':
    area = input("input artist name: ").strip()
    with open_db() as r:
        l = sum(1 for _ in query_music(r, 'area', '*', value_query=area))
    print(f'{l} items')
