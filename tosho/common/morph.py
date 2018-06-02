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
