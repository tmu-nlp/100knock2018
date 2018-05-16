import re
from knock20 import get_text

wiki_text = get_text()
findedList = re.findall('\[\[Category:([^\]]+)\]\]', wiki_text)
print(findedList)