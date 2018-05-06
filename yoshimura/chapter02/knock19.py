import sys

file_name = sys.argv[1]
file = open(file_name,"r")

dic = {}

# 一列めだけのリストを作成
lines = file.readlines()
list_pre = [line.split("\t")[0] for line in lines]

for line in list_pre:
    if line not in dic:
        dic[line] = 1
    else:
        dic[line] += 1

for word, count in sorted(dic.items(),key = lambda dic : dic[1], reverse = True):
    print(word.strip(),count)

# cut -f 1 hightemp.txt | sort | uniq -c | sort -r