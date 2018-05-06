from sys import argv

with open(argv[2]) as fr:
    for i, line in enumerate(fr):
        if i == int(argv[1]):
            exit()
        print(i, line, end = "")

# head -$1 filename
