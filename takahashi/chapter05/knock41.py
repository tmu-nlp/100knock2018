# -*- coding: utf-8 -*-
from Morph import Morph
from Chunk import Chunk
import pickle

sentences = []
sentence = []
chunk = None

with open('../data/neko.txt.cabocha', 'r', encoding="utf-8_sig") as f:
    for line in f:
        line = line.replace('\n', '')
        line_split = line.split()

        if line_split[0] == 'EOS':
            if chunk is not None:
                sentence.append(chunk)
            if len(sentence) > 0:
                sentences.append(sentence)
            chunk = None
            sentence = []
        elif line_split[0] == '*':
            if chunk is not None:
                sentence.append(chunk)
            chunk = Chunk(morphs=[], dst=int(line_split[2].replace('D', '')), srcs=int(line_split[1]))
        else:
            contents = line.split('\t')
            surface = contents[0]
            info = contents[1].split(',')
            base = info[6]
            pos = info[0]
            pos1 = info[1]
            _morph = Morph(surface, base, pos, pos1)
            chunk.morphs.append(_morph)

with open('../data/neko_sentences.pkl', 'wb') as f:
    pickle.dump(sentences, f)

for morphs in sentences[7]:
    print(str(morphs))