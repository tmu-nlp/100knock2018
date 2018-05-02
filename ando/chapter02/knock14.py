import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 25:
        print("wrong number of arguments")
        sys.exit()
    num=args[1]
    f = open("hightemp.txt").read()
    line=f.split("\n")
    for i in range(int(num)):
        print(line[i])
"""
head -n 5 hightemp.txt
"""