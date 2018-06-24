from knock60 import init_kvs, Music
from sys import argv

def main():

    r = init_kvs()
    if len(argv) > 1:
        place = argv[1]
        c = 0
        for music in query_place(r, place):
            print(f'{music.name}: {music.area}')
            c += 1

        print('='*50)
        print(f'{c} items')

def query_place(r, place):
    for name in r.scan_iter():
        area = r.get(name)
        if area == place:
            yield Music(name, area)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')