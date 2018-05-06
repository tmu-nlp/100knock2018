from itertools import zip_longest

col1 = open('col1.txt', 'r').readlines()
col2 = open('col2.txt', 'r').readlines()

out = open('out13.txt', 'w')

for c1, c2 in zip_longest(col1, col2):
    out.write(c1.replace('\n', '') + '\t' + c2)

# paste col1.txt col2.txt
