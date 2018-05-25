# -*- coding: utf-8 -*-


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f'surface:{self.surface} ' \
               f'base:{self.base} ' \
               f'pos:{self.pos} ' \
               f'pos1:{self.pos1}'

    def check_period(self):
        if self.pos1 != '句点' or self.pos1 != '読点':
            return True
        else:
            return False


def morpheme_list(text):
    sentence = []
    sentences = []
    for line in open(text, 'r'):
        line = line.split()
        if line[0] == 'EOS':
            sentences.append(sentence)
            sentence = []
        elif line[0] == '*':
            pass
        else:
            morpheme = line[0].split(',') + line[1].split(',')
            morph = Morph(
                surface=morpheme[0],
                base=morpheme[7],
                pos=morpheme[1],
                pos1=morpheme[2]
            )
            sentence.append(morph)

    return sentences


if __name__ == '__main__':
    text = 'neko.txt.cabocha'
    sentences = morpheme_list(text)
    for morpheme in sentences[2]:
        print(morpheme)
