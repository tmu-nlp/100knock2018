import re

p = re.compile('\[File[^\|]+')
p2 = re.compile('\[ファイル[^\|]+')
line = open("igirisu.txt").read()
m = re.findall(p,line)
for i in m:
    i = i.lstrip("[File:")
    print(i)
m = re.findall(p2,line)
for i in m:
    i = i.lstrip("[ファイル:")
    print(i)