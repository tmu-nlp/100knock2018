
def main():
    from knock64 import MusicDb

    db = MusicDb()
    name = input("input artist name: ").strip()
    found = db.collection.find({"area": name}).count()
    print(f'{found} artists found')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')