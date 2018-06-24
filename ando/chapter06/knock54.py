import sys
import knock53
import re


p = re.compile('<word>.+?\<')
p2 = re.compile('<lemma>.+?\<')
p3 = re.compile('<POS>.+?\<')

def parsexml():
    xml = knock53.parse().split("\n")
    lists = []
    for i in xml:
        if isinstance(re.search(p,i),type(None)):
            continue
        else:
            lists.append((re.search(p,i).group().replace("<word>","").replace("<",""),re.search(p2,i).group().replace("<lemma>","").replace("<",""),re.search(p3,i).group().replace("<POS>","").replace("<","")))
    return lists

if __name__ == "__main__":
    triple = parsexml()
    print(triple)