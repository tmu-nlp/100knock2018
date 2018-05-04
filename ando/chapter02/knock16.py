import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 25:
        print("wrong number of arguments")
        sys.exit()
    num=args[1]
    f = open("hightemp.txt").read()
    line=f.split("\n")
    q = 25 // int(num)
    mod = 25 % int(num)
    incre = 0
    for i in range(int(num),25,int(num)):
        if incre == q:
            break
        incre += 1
        for j in range(i-int(num),i):
            print(line[j])
        print("----------------------")
    for i in range(q*int(num),q*int(num)+mod):
        print(line[i])
"""
split -l 5 hightemp.txt
"""