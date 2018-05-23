# -*- coding: utf-8 -*-

from knock30 import load_mecab

path = 'neko.txt.mecab'

ans = []
noun = []
noun_phrase = []
for sentence in load_mecab(path):
    for i in range(len(sentence)):
        if sentence[i]['pos'] == '名詞':
            noun.append(sentence[i]['surface'])
        else:
            if len(noun) > 1:
                noun_phrase.append(''.join(noun))
            noun = []
    if len(noun) > 1:  # 文末が名詞のとき
                noun_phrase.append(''.join(noun))
    noun = []


print(noun_phrase)
