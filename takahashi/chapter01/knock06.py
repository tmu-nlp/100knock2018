# -*- coding: utf-8 -*-

str1 = "paraparaparadise"
str2 = "paragraph"

def get_n_gram(seq, n):
    ret = []
    for i in range(len(seq)):
        item = ''
        count = 0
        for j in range(n):
            if i + j < len(seq):
                item += seq[i + j]
                count += 1
            else:
                continue
        if count == n:
            ret.append(item)
    return ret

x = get_n_gram(str1, 2)
y = get_n_gram(str2, 2)
print(x)
print(y)


z = y.copy()
for item in x:
    if item in y:
        continue
    else:
        if item not in z:
            z.append(item)
print(z)

z = []
for item in x:
    if item in y:
        if item not in z:
            z.append(item)
    else:
        continue
print(z)

z = []
for item in x:
    if item in y:
        continue
    else:
        if item not in z:
            z.append(item)

print(z)


