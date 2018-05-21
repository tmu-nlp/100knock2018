import os,sys
sys.path.append(os.pardir)

from common.morph import Morph
from collections import defaultdict

# 名詞,一般,*,*,*,*,南無阿弥陀仏,ナムアミダブツ,ナムアミダブツ
base_index = 6
pos_index = 0
pos1_index = 1

def iterate_mecab_morphs(filename):
    with open(filename, 'r') as f:
        morphs = []
        for line in f:
            line = line.strip('\n')
            if line.upper() == 'EOS':
                # 文末に達した場合は、それまでの解析結果を返す
                yield morphs
                morphs = []
            else:
                morph = parse_mecab_line(line)
                morphs.append(morph)
        # 最後の文の形態素リストを返す
        yield morphs
            
def parse_mecab_line(line):
    word, props = line.split('\t')
    props = props.split(',')

    m = Morph()
    m.surface = word
    m.base = props[base_index]
    m.pos = props[pos_index]
    m.pos1 = props[pos1_index]

    return m
            
'''
Sample
==========
EOS
南無阿弥陀仏	名詞,一般,*,*,*,*,南無阿弥陀仏,ナムアミダブツ,ナムアミダブツ
南無阿弥陀仏	名詞,一般,*,*,*,*,南無阿弥陀仏,ナムアミダブツ,ナムアミダブツ
。	記号,句点,*,*,*,*,。,。,。
EOS
ありがたい	形容詞,自立,*,*,形容詞・アウオ段,基本形,ありがたい,アリガタイ,アリガタイ
ありがたい	形容詞,自立,*,*,形容詞・アウオ段,基本形,ありがたい,アリガタイ,アリガタイ
。	記号,句点,*,*,*,*,。,。,。
EOS
EOS
'''