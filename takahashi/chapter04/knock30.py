# -*- coding: utf-8 -*-
lines = []
morphemes = []

with open('../data/neko.txt.mecab', 'r', encoding='utf-8') as f:
    for line in f:
        if line == 'EOS\n':
            if len(morphemes) != 0:
                lines.extend([morphemes])
            morphemes = []
        else:
            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            surface = line.split('\t')[0]
            others = line.split('\t')[1]
            dict = {
                'surface': surface,
                'base': others.split(',')[6],
                'pos': others.split(',')[0],
                'pos1': others.split(',')[1],
            }
            morphemes.extend([dict])
            print(dict)
for i in range(0, 10):
    print(lines[i])