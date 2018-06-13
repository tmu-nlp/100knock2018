from knock30 import get_mecab_list

mecab_list = get_mecab_list()
result = []
i = 0
while i < len(mecab_list):
	if mecab_list[i]["pos"] == "名詞":
		noun_group = mecab_list[i]["surface"]
		while mecab_list[i+1]["pos"] == "名詞":
			noun_group += mecab_list[i+1]["surface"]
			i += 1
		result.append(noun_group)
	i += 1
		
# print(result[30:100])