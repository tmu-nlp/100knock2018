f = open("col1.txt").read()
f2 = open("col2.txt").read()
f = f.rstrip()
f2 = f2.rstrip()
col1 = f.split(" ")
col2 = f2.split(" ")
for i in range(len(col1)):
    with open("merge.txt", "a") as fout:
	    fout.write(col1[i] + "\t" + col2[i] + "\n")
"""
paste -d , col1.txt col2.txt
"""