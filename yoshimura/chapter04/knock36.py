import MeCab
from collections import defaultdict

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

words = defaultdict(lambda:0)
for sentence in result:
    for morpheme in sentence:
        words[morpheme['surface']] += 1

for key, value in sorted(words.items(), key = lambda x:x[1], reverse = True):
    print(f'{key}\t{value}')

