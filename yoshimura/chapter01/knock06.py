from knock05 import ngram

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(str1,2))
Y = set(ngram(str2,2))

print(f"XとYの和集合 : {X | Y}")
print(f"XとYの積集合 : {X & Y}")
print(f"XとYの差集合 : {X - Y}")

if {"se"} <= X:
    print(f"'se'はXに含まれる")
else:
    print("'se'はXに含まれない")

if {"se"} <= Y:
    print("'se'はYに含まれる")
else:
    print("'se'はYに含まれない")