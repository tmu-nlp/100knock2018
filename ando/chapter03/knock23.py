import re

p = re.compile('==+')
line = open("igirisu.txt").readlines()
for i in line:
    i = i.rstrip()
    m = re.match(p,i)
    if not isinstance(m,type(None)):
        level = i.count("=")
        i = re.sub(p,"",i)
        print(i+"\t"+str(level/2-1))