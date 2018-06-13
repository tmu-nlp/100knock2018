import CaboCha
from knock40 import Morph

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []
    
    def __str__(self):
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return(f'{surface} {self.dst} {self.srcs}')
    
    def normalized_surface(self):
        '''句読点などの記号を除いた表層を返す'''
        n_surface = ''
        for morph in self.morphs:
            if morph.pos != '記号':
                n_surface += morph.surface
        return n_surface
    
    def surface(self):
        '''表層を返す'''
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return surface
    
    def check_pos(self, pos):
        '''引数の品詞が含まれているたらTrueを返す'''
        for morph in self.morphs:
            if morph.pos == pos:
                return True
        return False
    
    def get_surfaces(self, feature, s):
        '''featureがsの表層形を全て返す'''
        morphs = []
        if feature == 'pos':
            for morph in self.morphs:
                if morph.pos == s:
                    morphs.append(morph.base)
            return morphs
        if feature == 'pos1':
            for morph in self.morphs:
                if morph.pos1 == s:
                    morphs.append(morph.base)
            return morphs

    def get_sahen_wo(self):
        '''「サ変接続名詞+を（助詞）」で構成される文節があればそれを返す'''
        for i in range(len(self.morphs) - 1):
            if self.morphs[i].pos1 == 'サ変接続' and self.morphs[i + 1].surface == 'を':
                return self.morphs[i].surface + self.morphs[i+1].surface
        return ''
    
    # def __eq__(self, other):
    #     if other is None or not isinstance(other, Chunk): 
    #         return False
    #     return self is other

        
        


        
def get_chunk_list():
    '''
     「吾輩は猫である」を係り受け解析した結果の各単語に
     ・形態素（Morphオブジェクト）のリスト(morphs)
     ・係り先文節インデックス番号（dst)
     ・係り元文節インデックス番号のリスト(srct)
     をメンバとするクラスのを作り、
    一文をそのChunkオブジェクトのリストとして、

    戻り値: 一文ごとのChunkクラスを要素とするリストを要素にもつリスト
    '''
    with open('neko.cabocha','r') as neko_file:
        result = []
        chunks = {} # Chunkオブジェクトのidx : Chunkオブジェクト
        for line in neko_file:
            line = line.rstrip() #stripだと先頭の空白文字が消える

            # 係り受け情報の場合
            if line[0] == '*':

                idx = int(line.split(' ')[1]) # 文節番号 
                dst = int(line.split(' ')[2][:-1]) # 係り先の文節番号（係り先なし:-1) 

                # Chunkオブジェクトをchunksに追加
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].dst = dst

                # 係り先があって係り先のオブジェクトが存在しなければ作成してそのsrcsに文節番号を追加
                if dst != -1:
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                    chunks[dst].srcs.append(idx)

            # 形態素情報の場合
            elif line != 'EOS' and line[:1] != '*':
                # lineの列をそれぞれリストに格納
                columm = line.split('\t')[1].split(',')
                columm.insert(0,line.split('\t')[0])
                
                # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
                morpheme = {'surface': columm[0], 'base': columm[7], 'pos': columm[1], 'pos1': columm[2]}
                chunks[idx].morphs.append(Morph(**morpheme))

            # 文の終わりの場合
            elif line == 'EOS' and len(chunks) != 0:
                sentence = [chunks[i] for i in sorted(chunks.keys())] #keyでソートしてvalueを取り出す
                result.append(sentence[:]) #chunksで渡すと次の行でappendしたものが消えてしまう
                chunks.clear()

    return result

if __name__ == '__main__':
    for i, chunk in enumerate(get_chunk_list()[7]):
        print(f'{i} {chunk}')