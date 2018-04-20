# -*- coding: utf-8 -*-

str = 'stressed'
ret = ''
for i in range(len(str)):
    ret += str[len(str) - i - 1]
print(ret)