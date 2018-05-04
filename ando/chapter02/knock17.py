col = []
f = open("hightemp.txt").read()
line=f.split("\n")
for i in line:
    i = i.split("\t")
    if i[0] not in col:
        col.append(i[0])
    else:
        continue
print(len(col))
"""
sort col1.txt | uniq
"""