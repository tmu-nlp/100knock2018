# -*- coding: utf-8 -*-
noun_articulation = []
flg = 0
phrase = ''

with open('../data/neko.txt.mecab', 'r', encoding='utf-8') as f:
    for line in f:
        if line == 'EOS\n':
            phrase = ''
            flg = 0
            pass
        else:
            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            # {'surface': '水', 'pos': '名詞', 'base': '水', 'pos1': '一般'}
            # {'surface': 'の', 'pos': '助詞', 'base': 'の', 'pos1': '連体化'}
            # {'surface': '中', 'pos': '名詞', 'base': '中', 'pos1': '非自立'}
            surface = line.split('\t')[0]
            pos = line.split('\t')[1].split(',')[0] # 品詞
            pos1 = line.split('\t')[1].split(',')[1] # 品詞細分類1
            if flg == 0 and pos == '名詞':
                phrase += surface
                flg = 1
            elif flg == 1 and pos == '名詞':
                phrase += surface
                flg = 2
            elif flg == 2 and pos != '名詞':
                noun_articulation.extend([phrase])
                phrase = ''
                flg = 0
            else:
                phrase = ''
                flg = 0

print(len(noun_articulation))
print(noun_articulation)

# for i in range(0, 10):
#     print()