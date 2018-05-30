# -*- coding: utf-8 -*-

from knock42 import srcs_dst_list
from knock41 import chunk_list

if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    list_ = srcs_dst_list(sentences)
    for line in list_:
        for pair in line:
            dst = pair[0].check_pos_phrase('名詞')
            srcs = pair[1].check_pos_phrase('動詞')
            if dst is not None and srcs is not None:
                print(f'{dst}\t{srcs}')
