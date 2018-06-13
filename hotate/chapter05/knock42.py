# -*- coding: utf-8 -*-

from knock41 import chunk_list


# 文ごとの　[(かかり元のChunk，かかり先のChunk), (かかり元のChunk，かかり先のChunk)]　のリストを返す
def srcs_dst_list(text):
    list_ = []
    for sentence in text:
        pair = []
        for i in range(len(sentence)):
            srcs = sentence[i]
            if srcs.dst == -1:
                pass
            else:
                dst = sentence[sentence[i].dst]
                pair.append((srcs, dst))
        list_.append(pair)
    return list_


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    list_srcs_dst = srcs_dst_list(sentences)
    with open('knock42.txt', 'w') as f:
        for line in list_srcs_dst:
            for pair in line:
                f.write(f'{pair[0].phrase_surface()}\t{pair[1].phrase_surface()}\n')
                # print(f'{pair[0].phrase_surface()}\t{pair[1].phrase_surface()}')
