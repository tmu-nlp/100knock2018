import re
from knock20 import get_text

wiki_text = get_text()

regex_str = '\[*[ファイル,File]:([^\|]+)'
level_list = re.findall(regex_str, wiki_text)

print(level_list)
