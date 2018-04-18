def gram(wlist):
    backlist = []
    for i in range(len(wlist)):
        if i == len(wlist)-1:
            return backlist
        backlist.append(wlist[i]+"-"+wlist[i+1])

seki = []
sa = []
w1 = "paraparaparadise"
w2 = "paragraph"
x = gram(list(w1))
x = list(set(x))
y = gram(list(w2))
y = list(set(y))
wa = gram(list(w1))
wa.extend(y)
wa = list(set(wa))
for i in x:
    if i in y:
        seki.append(i)
for i in wa:
    if i not in seki:
        sa.append(i)
print(wa)
print(seki)
print(sa)
if "s-e" in x:
    print("s-e is in x")
else:
    print("s-e is not in x")
if "s-e" in y:
    print("s-e is in y")
else:
    print("s-e is not in y")