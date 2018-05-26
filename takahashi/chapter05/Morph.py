# -*- coding: utf-8 -*-

class Morph():
    def __init__(self, surface='', base='', pos='', pos1=''):
        self.surface = surface  # 表層形
        self.base = base        # 基本形
        self.pos = pos          # 品詞
        self.pos1 = pos1        # 品詞細分類1

    def __str__(self):
        return 'surface:{0} base:{1} pos:{2} pos1:{3}'.format(self.surface, self.base, self.pos, self.pos1)

    def get_pos1(self):
        return self.pos1

    @property
    def is_verb(self):
        if self.pos == '動詞':
            return True
        return False

    @property
    def is_noun(self):
        if self.pos == '名詞':
            return True
        return False

    @property
    def is_noun_sahensetuzoku(self):
        if self.pos == '名詞' and self.pos1 == 'サ変接続':
            return True
        return False

    @property
    def is_particle(self):
        if self.pos == '助詞':
            return True
        return False

    @property
    def is_particle_wo(self):
        if self.pos == '助詞' and self.base == 'を':
            return True
        return False
