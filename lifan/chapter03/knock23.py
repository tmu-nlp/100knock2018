import re
from knock20 import get_text

wiki_text = get_text()
level_dict = {}
for i in range(2,6):
	regex_str = '\n={%d}([^=]+)={%d}\n' % (i,i)
	level_list = re.findall(regex_str, wiki_text)
	level_dict[i] = level_list
print(level_dict)