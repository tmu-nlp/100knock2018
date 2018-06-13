# -*- coding: utf-8 -*-
import pprint
import pickle

from Morph import Morph
from Chunk import Chunk


with open('../data/neko_sentences.pkl', 'rb') as f:
    sentences = pickle.load(f)

structures = []
structure = {}

for sentence in sentences:
    for chunk in sentence:
        chunk.del_punc()
        structure[chunk.srcs] = chunk
    structures.append(structure)
    structure = {}

idx = 5
body_lists = []
structure = structures[idx]

for i in range(len(structure)):
    if structure[i].has_noun() and i + 1 <= len(structure):
        for j in range(i + 1, len(structure)):
            body_list = [structure[i], structure[j]]
            if structure[j].has_noun():
                body_lists.append(body_list.copy())
# pprint.pprint([_list[0].surface + ', ' + _list[1].surface for _list in body_lists])

for body_list in body_lists:
    # pprint.pprint(body_list[0].surface + ', ' + body_list[1].surface)

    root_flg = False
    dst = body_list[0].dst
    # 根に至る経路にあるか判定する
    while dst != -1:
        if dst == body_list[1].srcs:
            root_flg = True
            break
        dst = structure[dst].dst

    # txt = body_list[0].xx_surface('X')
    txt = [body_list[0]]

    # もし根に至る経路上にあれば|を使わない
    if root_flg:
        dst = body_list[0].dst
        while dst != body_list[1].dst:
            txt.append(structure[dst])
            dst = structure[dst].dst
        str = txt[0].xx_surface('X')
        for i, item in enumerate(txt[1:]):
            if i == len(txt) - 2:
                str += ' -> {}'.format(item.yy_surface('Y'))
            else:
                str += ' -> {}'.format(item.surface)
    # もし根に至る経路上になければ|を使う
    else:
        dst = body_list[1].srcs
        while dst != -1:
            txt.append(structure[dst])
            dst = structure[dst].dst
        str = txt[0].xx_surface('X')
        for i, item in enumerate(txt[1:]):
            if i == 0:
                str += ' | {}'.format(item.xx_surface('Y'))
            elif i == len(txt) - 2:
                str += ' | {}'.format(item.surface)
            else:
                str += ' -> {}'.format(item.surface)
    print(str)

