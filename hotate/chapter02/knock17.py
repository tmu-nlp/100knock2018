from collections import defaultdict
f = open('hightemp.txt', 'r')
dic = defaultdict(lambda: 0)
line = [line.rstrip().split() for line in f.readlines()]
count = 0
list = []

for w in line:
    if  w[0] not in list:
        list.append(w[0])

print(list)

#cat hightemp.txt | cut -f 1 | sort | uniq

