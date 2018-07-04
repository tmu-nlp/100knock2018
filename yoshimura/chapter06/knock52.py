from stemming.porter2 import stem

for line in open('result51'):
    line = line.rstrip()
    print(f'{line}\t{stem(line)}')
