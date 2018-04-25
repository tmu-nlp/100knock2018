# -*- coding: utf-8 -*-
import random

x = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
x = x.replace('.', '').replace(':', '')
x = x.split(' ')
while "" in x:
    x.remove("")

head = x[0]
tail = x[-1]

x = x[1:-1]

random.shuffle(x)

x = [head] + x + [tail]

print(x)
print(head)
print(tail)