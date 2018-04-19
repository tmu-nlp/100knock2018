import re

texnum = []
w = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
w = re.sub('[,|.]',"",w)
w = w.split(" ")
for i in w:
    texnum.append(len(i))
print(texnum)