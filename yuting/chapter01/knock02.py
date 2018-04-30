str1 = "hello"
str2 = "world"
ans = "".join([c1 + c2 for c1, c2 in zip(str1, str2)])
print(ans)
