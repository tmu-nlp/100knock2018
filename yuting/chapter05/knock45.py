import knock41


def extractVerbPatern(sentence):
    lst = []
    for chunk in sentence:
        if chunk.include_pos('動詞'):
            src_chunks = [sentence[src] for src in chunk.srcs]
            src_chunks_case = list(filter(lambda src_chunks: src_chunks.morphs_of_pos1('格助詞'), src_chunks))
            if src_chunks_case:
                lst.append((chunk, src_chunks_case))
    return lst


if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    g = open("neko.extractVerb.txt","w")
    sentences = knock41.read_chunk(f)
    verbPatterns = []
    for sentence in sentences:
        verbPatterns.append(extractVerbPatern(sentence))

    for verbPattern in verbPatterns:
        for verb, src_chunks in verbPattern:
            v = verb.morphs_of_pos('動詞')[-1].base
            ps = [src_chunk.morphs_of_pos1('格助詞')[-1].base for src_chunk in src_chunks]
            p = " ".join(sorted(ps))
            g.write("%s\t%s" % (v, p)+'\n')
    f.close()
    g.close()