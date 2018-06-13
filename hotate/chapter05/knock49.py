# -*- coding: utf-8 -*-

from knock48 import srcs_dst_dict, extraction_noun
from knock41 import chunk_list


def extraction_path(sentences):
    result = []
    for sentence in sentences:
        for x_no, combi_x in enumerate(sentence):
            for y_no in range(x_no+1, len(sentence)):
                combi_y = sentence[y_no]  # combi_yはcombi_xより後ろの係り受けパス
                path = []

                if combi_x[-1] == combi_y[-1]:  #　最後の文字が一致
                    c = list(set(combi_x) & set(combi_y))  # ｘとｙの共通部分　積集合
                    k = combi_x[-len(c):len(combi_x)]  # 後ろから数えて積集合の要素数分だけ抜き出す
                    i = combi_x[:-len(c)]  # 積集合を取り除いたもの
                    j = combi_y[:-len(c)]

                    if len(j) is 0:  # 共通の文節が存在しない場合
                        i.append(k[0])
                    path.append(i)

                    if len(j) is not 0:  # 共通の文節が存在する場合
                        path.append(j)
                        path.append(k[:1])
                    result.append(path)
                else:
                    pass
    return result


def write(file, line):
    for k in range(len(line)):
        for i, phrase in enumerate(line[k]):
            if i == 0 and k == 0:
                x = 'X'
                file.write(f'{phrase.phrase_surface_xy(x)}')
            elif i == 0 and k == 1:
                y = 'Y'
                file.write(f'{phrase.phrase_surface_xy(y)}')
            elif len(line) == 1 and i == len(line[0]) - 1:  # 最後の文節
                file.write('Y')
            else:
                file.write(f'{phrase.phrase_surface()}')

            if i < len(line[k]) - 1:
                file.write(' -> ')
            elif len(line) != 1 and k != 2:
                file.write(' | ')
            else:
                file.write('\n')


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    dict_srcs_dst = srcs_dst_dict(sentences)
    nouns = extraction_noun(dict_srcs_dst)
    result = extraction_path(nouns)

    with open('knock49.txt', 'w') as f:
        for line in result:
            write(f, line)
