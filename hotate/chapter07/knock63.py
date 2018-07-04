# -*- coding: utf-8 -*-
import plyvel
import json
import pickle


def make_db():
    db = plyvel.DB('./db_knock63/', create_if_missing=True)
    for line in open('artist.json', 'r'):
        artisit_dic = json.loads(line)
        if 'name' in artisit_dic and 'tags' in artisit_dic:
            db.put(artisit_dic['name'].encode('utf-8'), pickle.dumps(artisit_dic['tags']))
    db.close()


def search_tags(name):
    db = plyvel.DB('./db_knock63/', create_if_missing=True)
    try:
        tags = pickle.loads(db.get(name.encode('utf-8')))
    except:
        tags = '入力されたアーティストは登録されていません'
    db.close()
    return tags


if __name__ == '__main__':
    # make_db()
    while True:
        input_ = input()
        if input_ == 'quit':
            break
        else:
            tags = search_tags(input_)
            print(f'tags : {tags}')
