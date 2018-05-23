class Morph:
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