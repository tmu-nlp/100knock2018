import MeCab

morpheme = {}
sentence = []
result = []
with open('neko.txt.mecab','r') as neko_file:
    for line in neko_file:
        line = line.rstrip() #stripだと先頭の空白文字が消える
        if line != 'EOS':
            # lineの列をそれぞれリストに格納
            columm = line.split('\t')[1].split(',')
            columm.insert(0,line.split('\t')[0])

            # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
            morpheme = {'surface': columm[0], 'base': columm[7], 'pos': columm[1], 'pos1': columm[2]}

            sentence.append(morpheme)
            if columm[2] == '句点':
                result.append(sentence[:]) #sentenceで渡すと次の行でappendしたものが消えてしまう
                sentence.clear()

np = []
for s in result:
    for i in range(len(s) - 2): # rangenの引数が0以下だと実行されない
        if s[i]['pos'] == '名詞' and s[i+1]['surface'] == 'の' and s[i+2]['pos'] == '名詞':
            np.append(s[i]['surface'] + s[i+1]['surface'] + s[i+2]['surface'])        

print(np)