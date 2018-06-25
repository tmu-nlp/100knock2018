from knock60 import init_kvs, Music
from knock61 import query_music
from sys import argv
import itertools

def main():
    area = input("input artist name: ").strip()
    r = init_kvs()
    l = sum(1 for _ in query_music(r, 'area', '*', value_query=area))

    print(f'{l} items')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')