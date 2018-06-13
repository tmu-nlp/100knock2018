import urllib.request
import re

p = re.compile('url=\"[^\"]+')
o=urllib.request.urlopen("http://ja.wikipedia.org/w/api.php?action=query&titles=File:Flag%20of%20the%20United%20Kingdom.svg&prop=imageinfo&&iiprop=url&format=xml").read()
o = str(o)
i = re.search(p,o)
print(i.group().lstrip("url=\""))