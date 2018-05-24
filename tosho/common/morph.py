class Morph:
    '''
    形態素を表すクラス
    '''
    def __init__(self):
        self.surface = None # 表層形
        self.base = None    # 基本形
        self.pos = None     # 品詞
        self.pos1 = None    # 品詞細分類１
    
    # definition of == (equals)
    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.surface == other.surface and \
                self.base == other.base and \
                self.pos == other.pos and \
                self.pos1 == other.pos1
        return False
    
    def __repr__(self):
        return f'{self.surface}\t{self.pos},{self.pos1},{self.base}'

class Chunk:
    '''
    文節を表すクラス
    '''
    def __init__(self, id, morphs, dst, srcs):
        self.id = id
        self.morphs = morphs
        self.dst = dst
        if dst < 0:
            self.dst = None
        self.srcs = srcs

    def __repr__(self):
        return f'* {self.id} {self.dst}D'

    def phrase(self, remove_symbol=False):
        if remove_symbol:
            morphs = filter(lambda m : m.pos != '記号', self.morphs)
        else:
            morphs = self.morphs

        return ''.join(map(lambda m: m.surface, morphs))
    
    def contains_pos(self, pos):
        return self.morph_of_pos(pos) is not None
    
    def morph_of_pos(self, pos):
        for m in self.morphs:
            if m.pos == pos:
                return m
        return None
