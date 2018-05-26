# -*- coding: utf-8 -*-
from Morph import Morph
from Chunk import Chunk
import pickle
import pydotplus as pdp
from ete3 import PhyloTree
from collections import defaultdict

with open('../data/neko_sentences.pkl', 'rb') as f:
    sentences = pickle.load(f)

for line_num, sentence in enumerate(sentences):
    original_sentence = ''
    for chunk in sentence:
        chunk.del_punc()
        original_sentence += chunk.surface

    verbs = {}
    dst_verb_list = []
    for chunk in sentence:
        chunk.del_punc()
        if not chunk.has_verb():
            continue
        else:
            for morph in chunk.morphs:
                if morph.is_verb:
                    verbs[morph.base] = chunk
                    break

    # verbsをdstにしているchunkがあるか
    # もしあってそこに助詞があればそれを拾ってくる
    dst_verb_dict = defaultdict(lambda: [])
    if len(verbs) > 0:
        for chunk in sentence:
            chunk.del_punc()
            for key in verbs.keys():
                if verbs[key].srcs == chunk.dst:
                    for morph in chunk.morphs:
                        if morph.is_particle:
                            dst_verb_dict[key].extend([morph.base])

    if len(dst_verb_dict) > 0:
        for key in dst_verb_dict.keys():
            items = ''
            for i, item in enumerate(dst_verb_dict[key]):
                items += item
                if i != len(dst_verb_dict[key]) - 1:
                    items += ' '
            print('{0}\t{1}'.format(key, items))
