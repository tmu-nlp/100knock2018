# -*- coding: utf-8 -*-

from knock41 import chunk_list


# 文ごとの　[{一文目のかかり元のChunk：かかり先のChunk}, {二文目のかかり元のChunk：かかり先のChunk}]　のリストを返す
def srcs_dst_dict(text):
    list_ = []
    for sentence in text:
        dic = {}
        for i in range(len(sentence)):
            srcs = sentence[i]
            if srcs.dst == -1:
                pass
            else:
                dst = sentence[sentence[i].dst]
                dic[srcs] = dst
        list_.append(dic)
    return list_


def extraction_noun(dict_srcs_dst):
    sentences = []
    for dic in dict_srcs_dst:
        sentence = []
        for srcs, dst in dic.items():
            combi = []
            phrase_srcs = srcs.check_pos_phrase('名詞')
            if phrase_srcs is not None:
                combi.append(srcs)
                combi.append(dst)
                combi = make_combi(combi, dic)
                sentence.append(combi)
            else:
                pass
        sentences.append(sentence)
    return sentences


# combiの続きを作る
def make_combi(combi, dic):
    if combi[-1].dst is not -1:
        combi.append(dic[combi[-1]])
        return make_combi(combi, dic)
    else:
        return combi


def write_file(combi, file_name):
    with open(file_name, 'w') as f:
        for line in combi:
            for pair in line:
                for i, phrase in enumerate(pair):
                    f.write(f'{phrase.phrase_surface()}')
                    if i < len(pair)-1:
                        f.write('　-> ')
                    else:
                        f.write('\n')


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    dict_srcs_dst = srcs_dst_dict(sentences)
    result = extraction_noun(dict_srcs_dst)
    write_file(result, 'knock48.txt')

