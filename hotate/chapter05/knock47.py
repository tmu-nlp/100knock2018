# -*- coding: utf-8 -*-

from knock42 import srcs_dst_list
from knock41 import chunk_list
from collections import defaultdict


def extraction_pos(list_srcs_dst):
    pair = []
    for line in list_srcs_dst:
        dic_pred = defaultdict(lambda: '')  # 動詞 : サ変接続名詞+を+動詞の基本形
        dic_srcs = defaultdict(lambda: '')  # 動詞 : かかり元(動詞にかかる助詞)
        dic_srcs_phrase = defaultdict(lambda: '')  # 動詞 : 動詞にかかる文節
        for phrase in line:
            phrase_sahen = phrase[0].check_sahen_wo()
            morph_verb = phrase[1].check_pos_morph('動詞')
            morph_srcs = phrase[0].check_pos_morph('助詞')
            phrase_srcs = phrase[0].check_pos_phrase('助詞')
            # 動詞がなかったら次のループへ
            if morph_verb is None:
                continue
            # サ変接続があったら辞書へ
            if phrase_sahen is not None:
                predicate = phrase_sahen + morph_verb
                dic_pred[morph_verb] = predicate
            # 助詞があったら辞書へ
            elif morph_srcs is not None:
                dic_srcs[morph_verb] += ' ' + morph_srcs
                dic_srcs_phrase[morph_verb] += ' ' + phrase_srcs

        for verb, srcs in dic_srcs.items():
            if verb in dic_pred.keys():
                pair.append([dic_pred[verb], srcs, dic_srcs_phrase[verb]])

    return pair


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    list_ = srcs_dst_list(sentences)
    with open('knock47.txt', 'w') as f:
        dic = extraction_pos(list_)
        for pair in dic:
            f.write(f'{pair[0]}\t{pair[1]}\t{pair[2]}\n')
