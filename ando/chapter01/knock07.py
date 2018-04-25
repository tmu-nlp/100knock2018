def bun(x2,y2,z2):
    sentence = "{}時の{}は{}".format(str(x2),str(y2),str(z2))
    return sentence
x=12
y="気温"
z=22.4
print(bun(x,y,z))