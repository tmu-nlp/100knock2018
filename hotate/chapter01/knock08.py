def cipher(x):
    ans = ""
    for c in x:
        if c.islower():
            c = chr(219-ord(c))
        ans += c
    return ans

s = "This is a pen"
s = cipher(s)
print(s)
print(cipher(s))

