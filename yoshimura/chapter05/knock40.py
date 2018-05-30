import CaboCha
import sys

class Morph:
    
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f'surface: {self.surface}\tbase: {self.base}\tpos: {self.pos}\tpos1: {self.pos1}'
    

def get_morpheme_list():
    '''
    「吾輩は猫である」を係り受け解析した結果の各単語を、
    表層形(surface)、基本形(base)、品詞(pos)、品詞分類１(pos1)
    をメンバとするクラスを作り、一文ずつでまとめてリストとして返す

    戻り値: 一文ごとのMorphクラスを要素とするリストのリスト
    '''
    morpheme = {} 
    sentence = []
    result = []
    with open('neko.cabocha','r') as neko_file:
        for line in neko_file:
            line = line.rstrip() #stripだと先頭の空白文字が消える
            if line != 'EOS' and line[:1] != '*':
                # lineの列をそれぞれリストに格納
                columm = line.split('\t')[1].split(',')
                columm.insert(0,line.split('\t')[0])

                # 上の二行はこれでも書ける
                # line = ','.join(line.split(\t)).split(',')

                # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
                morpheme = {'surface': columm[0], 'base': columm[7], 'pos': columm[1], 'pos1': columm[2]}

                sentence.append(Morph(**morpheme)) #Morphクラスをリストに追加
            if line == 'EOS' and len(sentence) != 0:
                result.append(sentence[:]) #sentenceで渡すと次の行でappendしたものが消えてしまう
                sentence.clear()
    return result

if __name__ == '__main__':
    for morph in get_morpheme_list()[2]: #3行目を出力
        print(morph)