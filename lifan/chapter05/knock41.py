from collections import defaultdict

class Morph:
	def __init__(self, surface, base, pos, pos1):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

class Chunk():
	def __init__(self, morphs, dst, srcs):
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs
		surface = ""
		for morph in self.morphs:
			surface += morph.surface
		self.surface = surface

	def __str__(self):
		return f"{self.surface}\tsrcs{self.srcs}\tdst[{self.dst}]"

def get_sentences():
	lines = open("../files/neko.txt.cabocha").readlines()
	sentences = []
	for i,line in enumerate(lines):
		line = line.strip()
		if i == 0:
			chunks = []
			morphs = []
			srcs_dict = defaultdict(list)
			dst = None
		if line[0] == "*":
			# 一個のchunk内にすべてのmorphsができたら、chunksにappendする
			chunks.append(Chunk(morphs, dst, []))
			# インデックスを抽出
			cols = line.split(" ")
			idx = int(cols[1])
			dst = int(cols[2][:-1])
			# idx=0を使って新しい文を判定する
			if idx == 0:
				# 係り元インデックス計算
				for i in range(0, len(chunks)):
					chunks[i].srcs = srcs_dict[i]
				# sentencesにchunksをappendし、chunksとsrcs_dictをクリア
				sentences.append(chunks)
				chunks = []
				srcs_dict = defaultdict(list)
			# 係り元インデックスをappendする
			srcs_dict[dst].append(idx)
			morphs = []

		# morphsに関する処理
		if line[0] != "*" and line != "EOS":
			splited_line = line.split("\t")
			if len(splited_line) == 1:
				splited_line.insert(0, '\t')
			surface = splited_line[0]
			feature = splited_line[1].split(',')
			base = feature[6]
			pos = feature[0]
			pos1 = feature[1]
			morph = Morph(surface, base, pos, pos1)
			morphs.append(morph)

		# 最後のラインの場合、chunksを追加
		elif i == len(lines):
				sentences.append(chunks)

	# 初期化のとき、残った一番目の空行を削除
	sentences.pop(0)
	return sentences

if __name__ == "__main__":
	sentences = get_sentences()
	for idx, chunk in enumerate(sentences[5]):
		print(idx, chunk)