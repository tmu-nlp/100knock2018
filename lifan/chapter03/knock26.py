import re
from knock20 import get_text
from knock25 import get_kiso

if __name__ == '__main__':
	# 強調マークアップの除去
	emphasize_mark = "'{3}"
	
	filter_regex = emphasize_mark
	result_dict = get_kiso(filter_regex)

# for key,value in result_dict.items():
# 	print("{}ーーー{}".format(key,value))