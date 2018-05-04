import sys


file_name = sys.argv[1]
file = open(file_name,"r")

lines = file.readlines()
lines.sort(key = lambda line : line.split("\t")[2],reverse = True)

for line in lines:
    print(line, end = "")

file.close()

#  sort -k 3 -r hightemp.txt
# keyは比較を行う前にリストの各要素に対して呼び出される関数を指定するパラメータ