import re
import requests
import ast
from knock20 import get_text
from knock25 import get_kiso

def get_response_json(file_name):
	params = {'action': 'query', 'format': 'json', 'prop': 'imageinfo', 'iiprop': 'url', 'titles': 'File:{}'.format(file_name)}
	response = requests.get('https://en.wikipedia.org/w/api.php', params)
	return response.json()

if __name__ == '__main__':
	# 強調マークアップの除去
	emphasize_mark = "'{3}"
	# 内部リンクの除去
	internal_link = "|\[\[|\]\]"
	# MediaWikiマークアップの除去
	media_mark = "|<.+>"
	filter_regex = emphasize_mark + internal_link + media_mark
	result_dict = get_kiso(filter_regex)

	flag_str = str(get_response_json(result_dict["国旗画像"]))
	imageinfo_str = re.findall(r"'imageinfo': \[\{(.+)\}\]", flag_str)[0]
	imageinfo_dic = ast.literal_eval("{"+ imageinfo_str +"}")

	print(imageinfo_dic["url"])
# print(flag_json["query"]["pages"]["23473560"]["imageinfo"][0]["url"])
