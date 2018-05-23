import os,sys
sys.path.append(os.pardir)

from common.morph import Morph, Chunk
from collections import defaultdict

# 名詞,一般,*,*,*,*,南無阿弥陀仏,ナムアミダブツ,ナムアミダブツ
base_index = 6
pos_index = 0
pos1_index = 1

def iterate_cabocha(filename):
    with open(filename, 'r') as f:
        chunks = []
        morphs = None   # 現在解析中の文節の形態素リスト（chunk.morphsへのポインタ）
        edges = []
        for line in f:
            line = line.strip('\n')
            if line.upper() == 'EOS':
                # 文末に達した場合は、それまでの解析結果を返す
                # todo: edges をまとめて、chunks をアップデートする
                # print(edges)
                for edge in edges:
                    src = edge[0]
                    dst = edge[1]

                    if dst > -1:
                        dst_chunk = chunks[dst]
                        dst_chunk.srcs.append(src)
                        # print(f'{dst_chunk} | {edge} | {dst_chunk.srcs}')

                yield chunks
                chunks = []
                edges = []
            elif line.startswith('*'):
                tags = line.split(' ')
                chunk_id = int(tags[1])
                dst_id = int(tags[2].replace('D', ''))

                chunk = Chunk(chunk_id, dst=dst_id, srcs=[], morphs=[])
                chunks.append(chunk)
                morphs = chunk.morphs
                edges.append((chunk_id, dst_id))
            else:
                morph = parse_mecab_line(line)
                morphs.append(morph)
        # 最後の文の形態素リストを返す
        yield chunks


def filter_mecab_result(filename, predicator):
    '''
    filter  Morph型のインスタンスを引数にとり、bool型を返すラムダ式
    '''
    for morphs in iterate_mecab_morphs(filename):
        for m in morphs:
            if predicator(m) == True:
                yield m

def iterate_mecab_morphs(filename):
    with open(filename, 'r') as f:
        morphs = []
        for line in f:
            if line.startswith('*'):
                continue
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
Sample(mecab)
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

sample(Cabocha)
==========
南無阿弥陀仏	名詞,一般,*,*,*,*,南無阿弥陀仏,ナムアミダブツ,ナムアミダブツ
。	記号,句点,*,*,*,*,。,。,。
EOS
* 0 1D 0/0 0.000000
ありがたい	形容詞,自立,*,*,形容詞・アウオ段,基本形,ありがたい,アリガタイ,アリガタイ
* 1 -1D 0/0 0.000000
ありがたい	形容詞,自立,*,*,形容詞・アウオ段,基本形,ありがたい,アリガタイ,アリガタイ
。	記号,句点,*,*,*,*,。,。,。
EOS
EOS

    吾輩は---------D
      ここで-D     |
        始めて-D   |
      人間という-D |
            ものを-D
              見た。

* 0 5D 0/1 -1.514009
吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
* 1 2D 0/1 1.311423
ここ	名詞,代名詞,一般,*,*,*,ここ,ココ,ココ
で	助詞,格助詞,一般,*,*,*,で,デ,デ
* 2 3D 0/1 0.123057
始め	動詞,自立,*,*,一段,連用形,始める,ハジメ,ハジメ
て	助詞,接続助詞,*,*,*,*,て,テ,テ
* 3 4D 0/1 1.440044
人間	名詞,一般,*,*,*,*,人間,ニンゲン,ニンゲン
という	助詞,格助詞,連語,*,*,*,という,トイウ,トユウ
* 4 5D 0/1 -1.514009
もの	名詞,非自立,一般,*,*,*,もの,モノ,モノ
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
* 5 -1D 0/1 0.000000
見	動詞,自立,*,*,一段,連用形,見る,ミ,ミ
た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
。	記号,句点,*,*,*,*,。,。,。
EOS
'''