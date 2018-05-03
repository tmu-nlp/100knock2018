
from sys import argv

col = int(argv[2])
s = set()
with open(argv[1]) as fr:
    for line in sorted(fr, key = lambda line: line.strip().split()[col]):
        print(line, end = "")
# without cat the columns
# t for field delim, k for key/field
# cat hightemp.txt | sort -t $'\t' -k 3 -r
