from collections import defaultdict


if __name__ == '__main__':
  count = defaultdict(int)
  for line in open('hightemp.txt'):
    line = line.split()[0]
    count[line] += 1
  for k, v in sorted(count.items(), key = lambda x:x[1], reverse = True):
    print(k, v)
  
