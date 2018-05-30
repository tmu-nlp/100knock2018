import knock41
import knock45

if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    g = open("neko.knock46.txt",'w')
    sentences = knock41.read_chunk(f)
    f.close()
    verbPatterns = []
    for sentence in sentences:
        verbPatterns.append(knock45.extractVerbPatern(sentence))

    for verbPattern in verbPatterns:
        
        for verb, src_chunks in verbPattern:
            col1 = verb.morphs_of_pos('動詞')[-1].base
            tmp = [(src_chunk.morphs_of_pos1('格助詞')[-1].base, str(src_chunk)) for src_chunk in src_chunks]
            tmp = sorted(tmp, key=lambda x:x[0])
            col2 = " ".join([col[0] for col in tmp])
            col3 = " ".join([col[1] for col in tmp])
            print("%s\t%s\t%s" % (col1, col2, col3))
        
#いる に   中に
#  に   上に
#いる  に   どこに
#切り落す    を   日月を
#する  を   天地を
#入る  に   太平に
#得る  を   太平を