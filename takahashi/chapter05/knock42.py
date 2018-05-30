# -*- coding: utf-8 -*-
from Morph import Morph
from Chunk import Chunk
import pickle

with open('../data/neko_sentences.pkl', 'rb') as f:
    sentences = pickle.load(f)

count = 0
paired_sentences = []
_paired_sentence = []

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
