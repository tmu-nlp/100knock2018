# -*- coding: utf-8 -*-

from knock42 import srcs_dst_list
from knock41 import chunk_list
from collections import defaultdict


# [pos1の形態素：pos2の形態素]を返す
# pos1：かかり元, pos2 : かかり先(pos1に係る)
def extraction_pos1(list_srcs_dst, pos_1, pos_2):
    pair = []
    for line in list_srcs_dst:
        dic_morph = defaultdict(lambda: '')  # 動詞：動詞に係る助詞
        dic_phrase = defaultdict(lambda: '')
        for phrase in line:
            morph_1 = phrase[1].check_pos_morph(pos_1)
            morph_2 = phrase[0].check_pos_morph(pos_2)
            phrase_2 = phrase[0].check_pos_phrase(pos_2)
            if morph_1 is None:
                continue
            if morph_2 is not None:
                # if morph_2 not in dic_morph[morph_1]:
                dic_morph[morph_1] += ' ' + morph_2
                dic_phrase[morph_1] += ' ' + phrase_2

        for k, v in dic_morph.items():
            pair.append([k, v, dic_phrase[k]])

    return pair


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    list_ = srcs_dst_list(sentences)
    with open('knock46.txt', 'w') as f:
        dic = extraction_pos1(list_, '動詞', '助詞')
        for pair in dic:
            f.write(f'{pair[0]}\t{pair[1]}\t{pair[2]}\n')
