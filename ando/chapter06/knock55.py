import sys
import knock53
import re


p = re.compile('<word>.+?\<')

def parsexml():
    xml = knock53.parse().split("\n")
    lists = []
    for i in xml:
        if isinstance(re.search(p,i),type(None)):
            continue
        elif "<NER>PERSON" in i:
            lists.append(re.search(p,i).group().replace("<word>","").replace("<",""))
    return lists

if __name__ == "__main__":
    person = parsexml()
    print(person)