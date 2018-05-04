col = []
col2 = []
f = open("hightemp.txt").read()
line=f.split("\n")
for i in line:
    i = i.split("\t")
    try:
        col.append(i[0])
        col2.append(i[1])
    except:
        break
colm = " ".join(col)
colm2 = " ".join(col2)
with open("col1.txt", "w") as fout:
	fout.write(colm)
with open("col2.txt", "w") as fout:
	fout.write(colm2)
"""
cut -f 1-2 hightemp.txt
"""