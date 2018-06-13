# -*- coding: utf-8 -*-

from knock30 import load_mecab

path = 'neko.txt.mecab'

ans = []
for sentence in load_mecab(path):
    for i in range(len(sentence)-1):
        if sentence[i-1]['pos'] == '名詞' and sentence[i]['pos1'] == '連体化' and sentence[i+1]['pos'] == '名詞':
            ans.append(sentence[i - 1]['surface'] + sentence[i]['surface'] + sentence[i + 1]['surface'])

print(ans)
