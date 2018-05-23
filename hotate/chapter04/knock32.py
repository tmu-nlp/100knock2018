# -*- coding: utf-8 -*-

from knock30 import load_mecab

path = 'neko.txt.mecab'

ans = []
for sentence in load_mecab(path):
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            ans.append(morpheme['base'])

print(ans)
