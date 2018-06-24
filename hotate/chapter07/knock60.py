# -*- coding: utf-8 -*-
import plyvel
import json


db = plyvel.DB('./db_knock60/', create_if_missing=True)
for line in open('artist.json', 'r'):
    artisit_dic = json.loads(line)
    if 'name' in artisit_dic and 'area' in artisit_dic:
        db.put(artisit_dic['name'].encode('utf-8'), artisit_dic['area'].encode('utf-8'))
db.close()
