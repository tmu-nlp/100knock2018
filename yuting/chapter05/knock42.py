#42. 係り元と係り先の文節の表示
import knock41

def make_chunk_pair(sentence):
    pairs = []
    for chunk in sentence:
        if chunk.dst != -1:
            pairs.append((chunk, sentence[chunk.dst]))
    return pairs

if __name__ == "__main__":
    f = open("neko.txt.cabocha")
    g = open("neko.make_chunk_pair.txt",'w')
    sentences = knock41.read_chunk(f)
    pair_sentences = []
    for sentence in sentences:
        pair = make_chunk_pair(sentence)
        pair_sentences.append(pair)
    for sentence in pair_sentences:
        for pair in sentence:
            g.write("\t".join([str(chunk) for chunk in pair])+'\n')
    f.close()
    g.close()