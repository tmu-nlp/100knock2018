# * 1 2D 0/1 -0.764522
# 吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ

# 一行目
# 1.*
# 2.文節番号
# 3.係り先の文節番号(係り先なし:-1)
# 4.主辞の形態素番号/機能語の形態素番号
# 5.係り関係のスコア(大きい方が係りやすい)

# 二行目
# 表層形（Tab区切り）品詞 品詞細分類1 品詞細分類2 品詞細分類3 活用形 活用型 原形 読み 発音

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

lines = open("../files/neko.txt.cabocha").readlines()
results = []
morphs = []
for i,line in enumerate(lines):
	# 新しい文の頭(または最後のライン)でmorphsを追加と初期化
	if line[:3] == "* 0" or i == len(lines):
		results.append(morphs)
		morphs = []

	if line[0] != "*" and line != "EOS\n":
		splited_line = line.strip().split("\t")
		if len(splited_line) == 1:
			splited_line.insert(0, '\t')
		surface = splited_line[0]
		feature = splited_line[1].split(',')
		base = feature[6]
		pos = feature[0]
		pos1 = feature[1]
		morph = Morph(surface, base, pos, pos1)
		morphs.append(morph)		

# 最初の空のmorphsを削除
results.pop(0)
for m in results[2]:
	print(m.surface, m.base, m.pos, m.pos1)
