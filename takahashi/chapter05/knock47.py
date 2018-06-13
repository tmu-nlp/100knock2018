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

    # 今回は文章をまたいでいるので、chunkをまたいで条件がそろったら格納する。
    # 格納するchunkは動詞にした（修飾先は動詞？）
    src = {}
    src_list = []
    flg = 0
    surface = ''
    for chunk in sentence:
        chunk.del_punc()
        for morph in chunk.morphs:
            if flg == 0 and morph.is_noun_sahensetuzoku:
                surface += morph.base
                flg = 1
            elif flg == 1 and morph.is_particle_wo:
                surface += morph.base
                flg = 2
            elif flg == 2 and morph.is_verb:
                surface += morph.base
                flg = 3
            else:
                surface = ''
                flg = 0

            if flg == 3:
                src[surface] = chunk

    # 格納したchunkに係る文節を探す
    dst_dict = defaultdict(lambda: [[], []])
    if len(src) > 0:
        for chunk in sentence:
            chunk.del_punc()
            for key in src.keys():
                if src[key].srcs == chunk.dst and src[key].srcs - 1 != chunk.srcs:
                    if len(chunk.morphs) > 0:
                        morph = chunk.morphs[-1]
                        if morph.is_particle:
                            dst_dict[key][0].extend([morph.base])
                            dst_dict[key][1].extend([chunk.surface])

    if len(dst_dict) > 0:
        for key in dst_dict.keys():
            particles = ''
            surfaces = ''
            item = dst_dict[key]
            for i, (particle, surface) in enumerate(zip(item[0], item[1])):
                particles += particle
                if i != len(item[0]) - 1:
                    particles += ' '
                surfaces += surface
                if i != len(item[1]) - 1:
                    surfaces += ' '
            print('{0}\t{1}\t{2}'.format(key, particles, surfaces))
