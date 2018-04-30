import sys

file_name = sys.argv[1]
file = open(file_name,"r")

dic = {}

lines = file.readlines()
for line in lines:
    if line not in dic:
        dic[line] = 1
    else:
        dic[line] += 1

for word, count in sorted(dic.items(),key = lambda dic : dic[1], reverse = True):
    print(word.strip(),count)

# cut -f 1 hightemp.txt | sort | uniq -c | sort -r