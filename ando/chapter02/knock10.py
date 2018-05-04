linenum = 0
f = open("/Users/one/Downloads/hightemp.txt").read()
line=f.split("\n")
for i in line:
  linenum += 1
print(linenum)
"""
wc -l hightemp.txt
"""