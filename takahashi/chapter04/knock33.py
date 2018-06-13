# -*- coding: utf-8 -*-
noun = {}

with open('../data/neko.txt.mecab', 'r', encoding='utf-8') as f:
    for line in f:
        if line == 'EOS\n':
            pass
        else:
            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            # {'pos': '名詞', 'surface': '見当', 'base': '見当', 'pos1': 'サ変接続'}
            surface = line.split('\t')[0]
            pos = line.split('\t')[1].split(',')[0] # 品詞
            pos1 = line.split('\t')[1].split(',')[1] # 品詞細分類1
            if pos == '名詞' and pos1 == 'サ変接続':
                if surface in noun:
                    noun[surface] += 1
                else:
                    noun[surface] = 1

print(len(noun))
print(noun.keys())

# for i in range(0, 10):
#     print()