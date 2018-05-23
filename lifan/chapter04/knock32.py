from knock30 import get_mecab_list

mecab_list = get_mecab_list()
result = []
for word_dict in mecab_list:
	if word_dict["pos"] == "動詞":
		result.append(word_dict["base"])
		
# print(result[1:10])