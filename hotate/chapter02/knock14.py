import sys

f = open('hightemp.txt', 'r')
n = int(sys.argv[1])

list = [line.strip() for line in f]

print(list[:n])

# head -n 6 'hightemp.txt'
