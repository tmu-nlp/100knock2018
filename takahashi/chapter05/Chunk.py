# -*- coding: utf-8 -*-

class Chunk():
    def __init__(self, morphs=[], dst=0, srcs=[]):
        self.morphs = morphs    # 形態素のリスト
        self.dst = dst          # 係り先文節インデックス番号
        self.srcs = srcs          # 係り元文節インデックス番号のリスト

    def __str__(self):
        return 'src:{0} dst:{1} morphs:{2}'.format(self.srcs, self.dst, ' / '.join([str(_morph) for _morph in self.morphs]))

    def _check_pos(self, _pos):
        for morph in self.morphs:
            if morph.pos == _pos:
                return True
        return False

    def del_punc(self):
        count = 0
        length = len(self.morphs)
        for i in range(length):
            if self.morphs[count].pos == '記号':
                self.morphs.pop(count)
            else:
                count += 1

    def has_punc(self):
        return self._check_pos('記号')

    def has_noun(self):
        return self._check_pos('名詞')

    def has_verb(self):
        return self._check_pos('動詞')

    @property
    def surface(self):
        txt = ''
        for morph in self.morphs:
            txt += morph.surface
        return txt

    def xx_surface(self, _x):
        txt = ''
        for i, morph in enumerate(self.morphs):
            if i == 0 and morph.is_noun:
                txt += _x
            else:
                txt += morph.surface
        return txt

    def yy_surface(self, _y):
        return _y

    @property
    def empty(self):
        if len(self.morphs) == 0:
            return True
        return False

