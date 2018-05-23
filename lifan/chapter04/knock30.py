# 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音


def get_mecab_list():
	result = []
	with open('../files/neko.txt.mecab','r', encoding='utf-8') as input_file:
		for line in input_file:
			line = line.strip()
			if line != "EOS":
				word_dict = {}
				splited_line = line.split('\t')
				if len(splited_line) == 1:
					splited_line.insert(0, "\t")
				surface = splited_line[0]
				feature = splited_line[1].split(',')
				word_dict["surface"] = surface
				word_dict["base"] = feature[6]
				word_dict["pos"] = feature[0]
				word_dict["pos1"] = feature[1]
				result.append(word_dict)
	return result



if __name__ == '__main__':
	mecab_list = get_mecab_list()
	print(mecab_list[0:10])