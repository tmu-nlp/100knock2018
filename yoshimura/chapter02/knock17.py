import sys

file_name = sys.argv[1]

file = open(file_name,"r")

count = 0
list = []
for line in file:
    if line not in list:
        list.append(line)
        count += 1

for word in sorted(list):
    print(word.strip())

# python knock17.py col1.txt | sort | uniq

# 14行目 list.sort()だとエラーが出る