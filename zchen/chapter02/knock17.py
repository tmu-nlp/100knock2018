from sys import argv

col = int(argv[2])
s = set()
with open(argv[1]) as fr:
    for line in fr:
        s.add(line.strip().split()[col])

print('\t'.join(s))

# line is the unit for sort by default
# unique/set will never be made without sort
# check more by examples in that book
# cut -d $'\t' -f 1 "hightemp.txt" | sort | uniq # -c with count number
