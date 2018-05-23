from collections import defaultdict
from knock30 import get_mecab_list

def get_ordered_words():
	mecab_list = get_mecab_list()
	result = defaultdict(lambda: 0)
	for word_dict in mecab_list:
		result[word_dict["base"]] += 1
	result = sorted(result.items(), key=lambda x: -x[1])
	return result

if __name__ == '__main__':
	ordered_words = get_ordered_words()
	# print(ordered_words[0:10])