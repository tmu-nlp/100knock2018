col3 = {}
f = open("hightemp.txt").read()
line=f.split("\n")
for i in range(len(line)):
    gyou = line[i].split("\t")
    try:
        col3[i] = float(gyou[2])
    except:
        break
o = sorted(col3.items(), key=lambda x: x[1])
for i in o:
    print(line[i[0]])
"""
sort -k 3,3 hightemp.txt
"""