
def main():
    from knock64 import MusicDb

    db = MusicDb()
    name = input("input artist name: ").strip()

    name_filter = {"name": name}
    alias_filter = {"aliases.name": name}
    exec_filter = {"$or": [name_filter, alias_filter]}

    for ret in db.find_artist(exec_filter):
        print(ret)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')