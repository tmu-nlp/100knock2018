from itertools import chain

class SNode:
    def __init__(self, tree):
        self.pos = tree[0]

        if len(tree) == 2 and isinstance(tree[1], str):
            self.children = tree[1]
            self.is_leaf = True
        else:
            self.children = [SNode(stree) for stree in tree[1:]]
            self.is_leaf = False
        
        # print(f'{self.is_leaf:<10}{self.pos:<10}{str(self.children)[:70]}')
        
    def __repr__(self):
        if self.is_leaf:
            return f'({self.pos} {self.children})'
        else:
            return f'({self.pos} {" ".join(map(str, self.children))})'

    def phrase(self):
        if self.is_leaf:
            return self.children
        else:
            return ' '.join(map(lambda c: c.phrase(), self.children))
    
    def findall(self, pos):
        # 子ノードを持つ場合はすべて検索する
        if self.is_leaf:
            nodes = []
        else:
            nodes = list(chain(*[n.findall(pos) for n in self.children]))
        
        # 自身が合致する場合は、検索結果に追加する
        if self.pos == pos:
            nodes.append(self)
        
        return nodes

class EnToken:
    def __init__(self, sentence_id=None, id=None, word=None, lemma=None, pos=None, ner=None):
        self.sentence_id = sentence_id
        self.id = id
        self.word = word
        self.lemma = lemma
        self.pos = pos
        self.ner = ner
    
    def __repr__(self):
        return '\t'.join([self.word, self.lemma, self.pos, self.ner])

class Mention:
    def __init__(self, sentence_id, start, end, head, text):
        self.sentence_id = sentence_id
        self.start = start
        self.end = end
        self.head = head
        self.text = text

class Coreference:
    def __init__(self, representative, mentions):
        self.representative = representative
        self.mentions = mentions

class Dependency:
    def __init__(self, dtype, governor, dependent):
        self.dtype = dtype
        self.governor = governor
        self.dependent = dependent
    
    def __repr__(self):
        return f'{self.dependent} -{self.dtype}-> {self.governor}'

class Morph:
    '''
    形態素を表すクラス
    '''
    def __init__(self):
        self.surface = None # 表層形
        self.base = None    # 基本形
        self.pos = None     # 品詞
        self.pos1 = None    # 品詞細分類１
    
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
        self.srcs = srcs

    def __repr__(self):
        return f'* {self.id} {self.dst}D'

    def phrase(self, remove_symbol=False, decorator=None):
        if remove_symbol:
            morphs = filter(lambda m : m.pos != '記号', self.morphs)
        else:
            morphs = self.morphs

        if decorator is None:
            return ''.join(map(lambda m: m.surface, morphs))
        else:
            return ''.join(map(lambda m: decorator(m), morphs))
    
    def contains_pos(self, pos, pos1=None, last=False):
        return self.morph_of_pos(pos, pos1, last) is not None
    
    def morph(self, pos, pos1=None, last=False):
        return self.morph_of_pos(pos, pos1, last)

    def morph_of_pos(self, pos, pos1=None, last=False):
        if last:
            morphs = reversed(self.morphs)
        else:
            morphs = self.morphs

        for m in morphs:
            if m.pos == pos and (pos1==None or m.pos1 == pos1):
                return m
        return None
    
    def append(self, morph):
        self.morphs.append(morph)
        return self
