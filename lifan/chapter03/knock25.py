import re
from knock20 import get_text
	
def get_kiso(filter_regex):
	wiki_text = get_text()

	pattern = r'{{基礎情報(.+)\n}}\n'
	compiled_string = re.compile(pattern, flags=(re.MULTILINE | re.DOTALL))

	finded_result = compiled_string.findall(wiki_text)

	if filter_regex != None:
		replaced_str = re.sub(filter_regex, "", finded_result[0])
	else:
		replaced_str = finded_result[0]

	finded_list = replaced_str.split('\n|')
	result_dict = {}
	for s in finded_list:
		each_dict = s.split(" = ")
		if len(each_dict) > 1:
			result_dict[each_dict[0]] = each_dict[1]
		else:
			result_dict["self"] = each_dict[0]
	return result_dict

if __name__ == '__main__':
	result_dict = get_kiso(None)

# for key,value in result_dict.items():
# 	print("{}ーーー{}".format(key,value))
