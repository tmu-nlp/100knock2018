from sys import argv

lines = []

with open(argv[2]) as fr:
    for line in enumerate(fr):
        if len(lines) <= int(argv[1]):
            lines.append(line)
        if len(lines) > int(argv[1]):
             # obsolete del in py3
            lines.pop(0)
for i, line in lines:
    print(i, line, end = "")

# tail -$1 "hightemp.txt"
