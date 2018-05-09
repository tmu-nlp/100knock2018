import re

dic = {}
line = open("igirisu.txt").readlines()
c=0
for i in line:
    if "基礎情報" in i:
        c=1
    if list(i)[0] == "|":
        i = i.lstrip("|")
        m = re.findall('\[\[[^\]]+',i)
        if len(m) != 0:
            for j in m:
                if "file" not in j and "ファイル" not in j:
                    if "|" not in j:
                        j += "]]"
                        i = i.replace(j,"")
                    else:
                        hyouji = j.split("|")
                        j += "]]"
                        i = i.replace(j,hyouji[1])
        i = re.sub('\'\'+',"",i)
        i = i.split(" = ")
        print(i)
        dic[i[0]] = i[1]
    if c==1:
        if i == "}}\n":
            break