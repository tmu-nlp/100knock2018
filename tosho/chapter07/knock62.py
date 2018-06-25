from knock60 import init_kvs, Music
from knock61 import query_music
from sys import argv
import itertools

def main():
    r = init_kvs()
    if len(argv) > 1:
        place = argv[1]
        l = sum(1 for _ in query_music(r, value_query=place))

        print(f'{l} items')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')