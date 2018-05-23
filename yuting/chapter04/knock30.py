#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
#各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
#1文を形態素（マッピング型）のリストとして表現せよ

def mecab_reader(mecabfile):
    sentences = []
    sentence = []
    for line in mecabfile:
        if line == "EOS\n":
            if len(sentence) > 0:
                sentences.append(sentence)
            sentence = []
        else:
            surface, features = line.split("\t")
            features = features.split(",")
            dic = {
                'surface': surface,
                'base': features[5],
                'pos': features[0],
                'pos1': features[1]
            }
            sentence.append(dic)
    return sentences

if __name__ == '__main__':
    inputfile = 'neko.txt.mecab'
    outputfile = 'neko.mecab_dic.txt'
    f = open(inputfile, 'r')
    g = open(outputfile, 'w')
    sentences = mecab_reader(f)

    for s in sentences:
        
        g.write(str(s) + "\n")

    f.close()
    g.close()