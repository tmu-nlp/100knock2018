f = open('hightemp.txt', 'r')
line = [line.rstrip().split() for line in f.readlines()]
line.sort(key = lambda x: x[2], reverse = True)
print(line)

#cat hightemp.txt | sort -r -k 3

