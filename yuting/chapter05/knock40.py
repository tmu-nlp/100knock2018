import CaboCha

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def print_all(self):
        return self.surface + "\t" + self.base + ", " + self.pos + ", " + self.pos1

def read_morpheme(cabochafile):
    sentences = []
    sentence = []
    for line in cabochafile:
        if line=="EOS\n":

            if len(sentence)>0:
                sentences.append(sentence)
                sentence= []
        elif line[0]=="*":
            pass
        else:
            surface, other = line.split("\t")
            others = other.split(",")
            base, pos, pos1 = others[6], others[0], others[1]
            morph = Morph(surface, base, pos, pos1)
            sentence.append(morph)

    return sentences

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = read_morpheme(f)
    for morph in sentences[1]:
        print (morph.print_all())


		
#吾輩  吾輩, 名詞, 代名詞
#は   は, 助詞, 係助詞
#猫   猫, 名詞, 一般
#で   だ, 助動詞, *
#ある  ある, 助動詞, *
#。   。, 記号, 句点		

#40. 係り受け解析結果の読み込み（形態素）
#形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
# さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

