file = open('hightemp.txt')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for line in file:
    words = line.strip().split()
    col1.write(words[0])
    col1.write('\n')
    col2.write(words[1])
    col2.write('\n')

# cut -f 2 'hightemp.txt'

