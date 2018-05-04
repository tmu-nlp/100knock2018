# -*- coding: utf-8 -*-
surfaces = {}
bases = {}

with open('../data/neko.txt.mecab', 'r', encoding='utf-8') as f:
    for line in f:
        if line == 'EOS\n':
            pass
        else:
            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            surface = line.split('\t')[0]
            if surface in surfaces:
                surfaces[surface] += 1
            else:
                surfaces[surface] = 1

            base = line.split('\t')[1].split(',')[6] # 原型
            if base in bases:
                bases[base] += 1
            else:
                bases[base] = 1

sorted(surfaces.items(), key=lambda x: x[1], reverse=True)
sorted(bases.items(), key=lambda x: x[1], reverse=True)

print(len(surfaces))
print(sorted(surfaces.items(), key=lambda x: x[1], reverse=True))
print(len(bases))
print(sorted(bases.items(), key=lambda x: x[1], reverse=True))

# for i in range(0, 10):
#     print()