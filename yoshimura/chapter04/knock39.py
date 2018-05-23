import MeCab
from collections import defaultdict
from matplotlib import pyplot as plt

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


hist = defaultdict(lambda:0) # 出現回数 : 単語の種類
for key, value in words.items():
    hist[value] += 1

d = sorted(hist.items(), key = lambda x:x[1], reverse = True)

word_count = [d[i][0] for i in range(len(d))] #key
word_type = [d[i][1] for i in range(len(d))]  #value


plt.loglog(sorted(words.values(),reverse = True))
plt.show()

# plt.rcParams['font.family'] = 'AppleGothic'
# plt.scatter(word_count, word_type)
# plt.xlabel("出現頻度")
# plt.ylabel("種類")
# plt.grid(True)
# plt.xscale('log')
# plt.yscale('log')
# plt.show()


