from collections import defaultdict
f = open('hightemp.txt', 'r')
line = [line.rstrip().split() for line in f.readlines()]
dic = defaultdict(lambda: 0)

for w in line:
    if  dic[w[0]] == 0:
        dic[w[0]] = 1
    else:
        dic[w[0]] += 1

for w, n in sorted(dic.items(), key=lambda x: x[1], reverse=True):
    print(f'{w} {n}')

# cat hightemp.txt | cut -f 1 | sort | uniq -c | sort -r -k1
