from knock30 import get_mecab_list

mecab_list = get_mecab_list()
result = []
for i in range(0, len(mecab_list)):
	if mecab_list[i]["pos1"] == "連体化":
		result.append( mecab_list[i-1]["surface"] + "の" + mecab_list[i+1]["surface"] )
		
# print(result[1:10])