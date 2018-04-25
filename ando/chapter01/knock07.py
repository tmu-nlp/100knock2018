import sys

def bun(x2,y2,z2):
    sentence = "{}時の{}は{}".format(str(x2),str(y2),str(z2))
    return sentence

args = sys.argv
x=args[1]
y=args[2]
z=args[3]
print(bun(x,y,z))
