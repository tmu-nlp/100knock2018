# -*- coding: utf-8 -*-

from knock30 import load_mecab
from collections import defaultdict


def morpheme_count(sentences):
    count = defaultdict(lambda: 0)
    for sentence in sentences:
        for morpheme in sentence:
            count[morpheme['surface']] += 1
    return count


if __name__ == '__main__':
    path = 'neko.txt.mecab'
    for morpheme, count in sorted(morpheme_count(load_mecab(path)).items(), key=lambda x: -x[1]):
        print(f'{morpheme} {count}')
