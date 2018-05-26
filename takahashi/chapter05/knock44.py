# -*- coding: utf-8 -*-
from Morph import Morph
from Chunk import Chunk
import pickle
import pydotplus as pdp
from ete3 import PhyloTree

with open('../data/neko_sentences.pkl', 'rb') as f:
    sentences = pickle.load(f)

count = 0
paired_sentences = []
_paired_sentence = []
dot_path = '../data/neko_sentences.dot'
dot_encoding = "utf-8_sig"

for sentence in sentences:
    if len(_paired_sentence) > 0:
        paired_sentences.append(_paired_sentence)
        _paired_sentence = []
    for chunk in sentence:
        if chunk.dst == -1:
            continue
        else:
            chunk.del_punc()
            chunk_dst = sentence[chunk.dst]
            chunk_dst.del_punc()
            if len(chunk.morphs) > 0 and len(chunk_dst.morphs) > 0:
                _paired_sentence.append([chunk, chunk_dst])
                print('{0} [src]{1}\t[dst]{2}'.format(count, str(chunk.surface), str(chunk_dst.surface)))
                count += 1

def sentence_to_dot(idx):
    head = "digraph sentence{} ".format(idx)
    body_head = "{ graph [rankdir = LR]; "
    body_head += 'node [fontname="arialuni.ttf"] '
    body_list = []
    for pair in paired_sentences[idx]:
        body_list.append('"{}"->"{}"; '.format(pair[0].surface, pair[1].surface))

    return head + body_head + ''.join(body_list) + '}'

idx = 4
dots = sentence_to_dot(idx)
g = pdp.graph_from_dot_data(dots)
g.write_jpeg('../data/neko_sentence{}_graph.jpg'.format(idx), prog='dot')
