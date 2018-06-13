# -*- coding: utf-8 -*-


def load_mecab(path):
    f_in = open(path, 'r')
    ans = []
    sentence = []
    for line in f_in:
        line = line.split('\t')
        if len(line) < 2:
            if len(sentence) > 0:
                ans.append(sentence)
            sentence = []
        else:
            morpheme = line[1].split(',')
            dic = {
                'surface': line[0],
                'base': morpheme[6],
                'pos': morpheme[0],
                'pos1': morpheme[1]
            }
            sentence.append(dic)

    return ans


if __name__ == '__main__':
    path = 'neko.txt.mecab'

    print(load_mecab(path))
