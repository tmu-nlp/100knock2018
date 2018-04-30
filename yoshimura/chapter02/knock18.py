import sys

file_name = sys.argv[1]
file = open(file_name,"r")

lines = file.readlines()
lines.sort(key = lambda line : line.split("\t")[2],reverse = True)

for line in lines:
    print(line, end = "")

file.close()

#  sort -k 3 -r hightemp.txt