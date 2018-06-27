# -*- coding: utf-8 -*-
import plyvel


def search_japan():
    db = plyvel.DB('./db_knock60/', create_if_missing=True)
    artist_num = 0
    for name, area in db:
        if area == 'Japan'.encode('utf-8'):
            artist_num += 1
    db.close()
    return artist_num


if __name__ in '__main__':
    print(search_japan())