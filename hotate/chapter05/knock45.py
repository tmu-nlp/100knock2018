# -*- coding: utf-8 -*-

from knock42 import srcs_dst_list
from knock41 import chunk_list
from collections import defaultdict


# [pos1の形態素：pos2の形態素]を返す
# pos1：かかり先, pos2 : かかり元(pos1に係る)
def extraction_pos(list_srcs_dst, pos_1, pos_2):
    pair = []
    for line in list_srcs_dst:
        dic = defaultdict(lambda: '')  # 動詞：動詞に係る助詞
        for phrase in line:
            morph_1 = phrase[1].check_pos_morph(pos_1)
            morph_2 = phrase[0].check_pos_morph(pos_2)
            if morph_1 is not None and morph_2 is not None:
                dic[morph_1] += ' ' + morph_2
        for k, v in dic.items():
            pair.append([k, v])
    return pair


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    list_ = srcs_dst_list(sentences)
    with open('knock45.txt', 'w') as f:
        list_pair = extraction_pos(list_, '動詞', '助詞')
        for pair in list_pair:
            f.write(f'{pair[0]}\t{pair[1]}\n')

# コーパス中で頻出する述語と格パターンの組み合わせ
# sort knock45.txt | uniq -c | sort -r

# する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
# sort knock45.txt | grep 'する' | uniq -c | sort -r
