import sys

def bun(x2,y2,z2):
    sentence = "{}時の{}は{}".format(str(x2),str(y2),str(z2))
    return sentence

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("wrong number of arguments")
        sys.exit()
    x=args[1]
    y=args[2]
    z=args[3]
    print(bun(x,y,z))
