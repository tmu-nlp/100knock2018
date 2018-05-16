import re

dic = {}
line = open("igirisu.txt").readlines()
c=0
for i in line:
    if "基礎情報" in i:
        c=1
    if list(i)[0] == "|":
        i = i.lstrip("|")
        i = i.split(" = ")
        print(i)
        dic[i[0]] = i[1]
    if c==1:
        if i == "}}\n":
            break