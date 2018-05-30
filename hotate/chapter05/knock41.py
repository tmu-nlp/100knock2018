# -*- coding: utf-8 -*-

from knock40 import Morph


class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = None
        self.srcs = None

    def __str__(self):  # 形態素区切り　→　分節区切り
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return f'{surface} dst:{self.dst} srcs:{self.srcs}'

    def phrase_surface(self):  # 形態素区切り　→　分節区切り
        surface = ''
        for morph in self.morphs:
            if morph.check_period():
                surface += morph.surface
        return f'{surface}'

    def phrase_surface_xy(self, n):  # 形態素区切り　→　分節区切り
        surface = ''
        for i, morph in enumerate(self.morphs):
            if morph.check_period():
                if i == 0:
                    surface += n
                else:
                    surface += morph.surface
        return f'{surface}'

    def phrase_surface_y(self):  # 形態素区切り　→　分節区切り
        surface = ''
        for i, morph in enumerate(self.morphs):
            if morph.check_period():
                if i == 0:
                    surface += n
                else:
                    surface += morph.surface
        return f'{surface}'

    def check_pos_phrase(self, pos):  # posに当てはまる形態素を含む文節を返す
        flag = False
        for morph in self.morphs:
            if morph.pos == pos:
                flag = True
            else:
                pass
        if flag:
            surface = self.phrase_surface()
            return surface
        else:
            return None

    def check_pos_morph(self, pos):  # posに当てはまる形態素を返す
        for morph in self.morphs:
            if morph.pos == pos:
                return morph.base
            else:
                pass
        return None

    def check_sahen_wo(self):  # サ変接続＋を　を含む文節を返す
        flag = False
        for morph in self.morphs:
            if morph.pos1 == 'サ変接続':
                flag = True
            if flag and morph.surface == 'を':
                surface = self.phrase_surface()
                return surface
            else:
                pass
        return None


def chunk_list(text):
    sentences = []
    sentence = []
    phrase = Chunk()
    for line in open(text, 'r'):
        line = line.split()
        if line[0] not in '*' and line[0] not in 'EOS':
            l = line[0].split(',') + line[1].split(',')
            morph = Morph(
                surface=l[0],
                base=l[7],
                pos=l[1],
                pos1=l[2]
            )
            phrase.morphs.append(morph)
        else:
            if len(phrase.morphs) > 0:
                sentence.append(phrase)
                phrase = Chunk()
            if line[0] == '*':
                phrase.dst = int(line[2].strip('D'))
            elif line[0] == 'EOS':
                for no, s in enumerate(sentence, 0):  # dstからsrcsを設定
                    sentence[s.dst].srcs = no
                sentences.append(sentence)
                sentence = []

    return sentences


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = chunk_list(text)
    for i, morpheme in enumerate(sentences[7]):
        print(f'{i} {morpheme}')
    # for sentence in sentences:
    #     for i, morpheme in enumerate(sentence):
    #         print(f'{i} {morpheme}')
