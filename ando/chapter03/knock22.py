import re

line = open("igirisu.txt").readlines()
for i in line:
    if "[[Category:" in i:
        i = i.lstrip("[[Category:")
        m = re.search('.+(?<!])',i)
        print(m.group())