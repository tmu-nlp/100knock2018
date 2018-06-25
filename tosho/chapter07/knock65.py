'''
docker exec -it mongo mongo

use chapter07
db.artists.find({"name": "Queen"})
'''

def main():
    from knock64 import MusicDb

    db = MusicDb()
    name = input("input artist name: ").strip()
    for ret in db.find_artist({"name": name}):
        print(ret)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')