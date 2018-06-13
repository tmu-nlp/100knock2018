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
    # もしあってその最後が助詞であればそれを拾ってくる
    dst_verb_dict = defaultdict(lambda: [[], []])
    if len(verbs) > 0:
        for chunk in sentence:
            chunk.del_punc()
            for key in verbs.keys():
                if verbs[key].srcs == chunk.dst:
                    if len(chunk.morphs) > 0:
                        morph = chunk.morphs[-1]
                        if morph.is_particle:
                            dst_verb_dict[key][0].extend([morph.base])
                            dst_verb_dict[key][1].extend([chunk.surface])

    if len(dst_verb_dict) > 0:
        for key in dst_verb_dict.keys():
            particles = ''
            surfaces = ''
            item = dst_verb_dict[key]
            for i, (particle, surface) in enumerate(zip(item[0], item[1])):
                particles += particle
                if i != len(item[0]) - 1:
                    particles += ' '
                surfaces += surface
                if i != len(item[1]) - 1:
                    surfaces += ' '
            print('{0}\t{1}\t{2}'.format(key, particles, surfaces))
