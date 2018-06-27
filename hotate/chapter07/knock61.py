# -*- coding: utf-8 -*-
import plyvel


def search_area(name):
    db = plyvel.DB('./db_knock60/', create_if_missing=True)
    try:
        area = db.get(name.encode('utf-8')).decode('utf-8')
    except:
        area = '入力されたアーティストは登録されていません'
    db.close()
    return area


if __name__ in '__main__':
    while True:
        input_ = input()
        if input_ == 'quit':
            break
        else:
            area = search_area(input_)
            print(f'area : {area}')
