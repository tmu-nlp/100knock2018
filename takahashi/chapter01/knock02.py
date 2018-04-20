# -*- coding: utf-8 -*-

str1 = 'パトカー'
str2 = 'タクシー'
ret = ''
for i in range(min(len(str1), len(str2))):
    ret += str1[i] + str2[i]
print(ret)