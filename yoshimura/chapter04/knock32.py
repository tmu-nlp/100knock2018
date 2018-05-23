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

ori_verb = []
for sentence in result:
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            ori_verb.append(morpheme['base'])

print(ori_verb)