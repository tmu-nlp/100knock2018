# -*- coding: utf-8 -*-
from Morph import Morph
from Chunk import Chunk

import pickle

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
body_list = []
structure = structures[idx]
for i in range(len(structure)):
    txt = ''
    dst = i
    if structure[i].has_noun():
        while dst != -1:
            txt += structure[dst].surface
            dst = structure[dst].dst
            if dst != -1:
                txt += ' -> '
        print(txt)
