col = {}
f = open("hightemp.txt").read()
line=f.split("\n")
for i in line:
    i = i.split("\t")
    if i[0] not in col:
        col[i[0]] = 1
    else:
        col[i[0]] += 1
o = sorted(col.items(), key=lambda x: x[1], reverse=True)
for i in o:
    print(i[0] + ":" + str(i[1]))
"""
cut -f 1-1 hightemp.txt | sort | uniq -c | sort -r
"""