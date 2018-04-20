# -*- coding: utf-8 -*-

str = 'パタトクカシーー'
index = [1,3,5,7]
ret = ''
for i in index:
    ret += str[i - 1]
print(ret)