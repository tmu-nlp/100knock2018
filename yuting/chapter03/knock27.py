import re
import json
from knock25 import fundamental_data
from knock26 import remove_emphasis

def remove_internalLink(string):
    internallink = re.compile(r"\[\[((.+?)\|)?(.+?)\]\]")
    emphasis_removed = remove_emphasis(string)
    return internallink.sub(r"\3", emphasis_removed)

if __name__ == "__main__":
    inputfile = 'jawiki.txt'
    outputfile = 'jawiki-linkmark.json'
    f = open(inputfile)
    res = fundamental_data(f, remove_internalLink)
    with open(outputfile, 'w') as g:
        json.dump(res, g, ensure_ascii=False)







#内部リンクマークアップ除去