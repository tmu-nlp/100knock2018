import knock40

class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __repr__(self):
        if self.morphs:
            surfs = [morph.surface for morph in self.morphs if morph.pos != '記号']
            return "".join(surfs)

    def include_pos(self, pos):
        return pos in [morph.pos for morph in self.morphs]

    def morphs_of_pos(self, pos):
        return [morph for morph in self.morphs if morph.pos == pos]

    def morphs_of_pos1(self, pos1):
        return [morph for morph in self.morphs if morph.pos1 == pos1]


def read_chunk(cabochafile):
    sentences = []
    sentence = []
    for line in cabochafile:
        if line == "EOS\n":
            for idx, c in enumerate(sentence[:-1]):
                if c.dst != -1:
                    sentence[c.dst].srcs.append(idx)
            # if len(sentence) > 1:
                # sentences.append(sentence)
            sentences.append(sentence)
            sentence = []
            
        elif line[0] == "*":
            chunk = Chunk()
            chunk.dst = int(line.split()[2].strip("D"))
            sentence.append(chunk)
        else:
            surface, other = line.split("\t")
            others = other.split(",")
            base, pos, pos1 = others[6], others[0], others[1]
            morph = knock40.Morph(surface, base, pos, pos1)
            sentence[-1].morphs.append(morph)
    return sentences


if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = read_chunk(f)
    for idx, chunk in enumerate(sentences[7]):
        surfaces = ""
        for mrph in chunk.morphs:
            surfaces += mrph.surface
        print ("%d" % idx, surfaces, "=>", chunk.dst)
    f.close()

#0 吾輩は => 5
#1 ここで => 2
#2 始めて => 3
#3 人間という => 4
#4 ものを => 5
#5 見た。 => -1

#EOS
#* 0 5D 0/1 -1.514009
#吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ
#は	助詞,係助詞,*,*,*,*,は,ハ,ワ
#* 1 2D 0/1 1.311423
#ここ	名詞,代名詞,一般,*,*,*,ここ,ココ,ココ
#で	助詞,格助詞,一般,*,*,*,で,デ,デ
#* 2 3D 0/1 0.123057
#始め	動詞,自立,*,*,一段,連用形,始める,ハジメ,ハジメ
#て	助詞,接続助詞,*,*,*,*,て,テ,テ
#* 3 4D 0/1 1.440044
#人間	名詞,一般,*,*,*,*,人間,ニンゲン,ニンゲン
#という	助詞,格助詞,連語,*,*,*,という,トイウ,トユウ
#* 4 5D 0/1 -1.514009
##もの	名詞,非自立,一般,*,*,*,もの,モノ,モノ
#を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
#* 5 -1D 0/1 0.000000
#見	動詞,自立,*,*,一段,連用形,見る,ミ,ミ
#た	助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
#。	記号,句点,*,*,*,*,。,。,。
#EOS