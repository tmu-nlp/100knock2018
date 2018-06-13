# -*- coding: utf-8 -*-
from Morph import Morph

sentences = []
sentence = []

with open('../data/neko.txt.cabocha', 'r', encoding="utf-8_sig") as f:
    for line in f:
        line = line.replace('\n', '')
        line_split = line.split()

        if line_split[0] == 'EOS' or line_split[0] == '*':
            pass
        else:
            contents = line.split('\t')
            surface = contents[0]
            info = contents[1].split(',')
            base = info[6]
            pos = info[0]
            pos1 = info[1]
            _morph = Morph(surface, base, pos, pos1)
            sentence.append(_morph)

            if _morph.get_pos1() == '句点':
                sentences.append(sentence)
                sentence = []

for morph in sentences[2]:
    print(str(morph))
