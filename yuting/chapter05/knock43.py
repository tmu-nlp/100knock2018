#43. 名詞を含む文節が動詞を含む文節に係るものを抽出

import knock41
import knock42

def findNtoV(chunk_pair):
    flagN = False
    flagV = False
    if "名詞" in [morph.pos for morph in chunk_pair[0].morphs]:
        flagN = True
    if "動詞" in [morph.pos for morph in chunk_pair[1].morphs]:
        flagV = True
    return flagN and flagV

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    g = open("neko.findNtoV.txt",'w')
    sentences = knock41.read_chunk(f)
    pair_sentences = []
    for sentence in sentences:
        pair = knock42.make_chunk_pair(sentence)
        pair_sentences.append(pair)
    pairs_NtoV = []
    for pair_sentence in pair_sentences:
        for chunk_pair in pair_sentence:
            if findNtoV(chunk_pair):
                pairs_NtoV.append(chunk_pair)
    for pair_NtoV in pairs_NtoV:
        noun, verb = pair_NtoV
        g.write("%s\t%s" % (noun, verb)+'\n')
    f.close()
    g.close()
