#動詞の原形をすべて抽出せよ

import knock30

def extract_verb_base(sentences):
    res = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['base'] == '基本形' and morpheme['pos']=='動詞':
                res.append(morpheme['surface'])
    return res

if __name__ == "__main__":
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_verb_base.txt'
    f = open(inputfile, "r")
    g = open(outputfile, "w")
    sentences = knock30.mecab_reader(f)
    res = extract_verb_base(sentences)
    for verb in res:
        
        g.write(verb + '\n')
    
    f.close()
    g.close()
