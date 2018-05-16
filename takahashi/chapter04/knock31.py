# -*- coding: utf-8 -*-
verb_surfaces = {}


with open('../data/neko.txt.mecab', 'r', encoding='utf-8') as f:
    for line in f:
        if line == 'EOS\n':
            pass
        else:
            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            surface = line.split('\t')[0]
            pos = line.split('\t')[1].split(',')[0] # 品詞
            if pos == '動詞':
                if surface in verb_surfaces:
                    verb_surfaces[surface] += 1
                else:
                    verb_surfaces[surface] = 1

print(len(verb_surfaces))
print(verb_surfaces.keys())

# for i in range(0, 10):
#     print()