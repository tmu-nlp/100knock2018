# -*- coding: utf-8 -*-
ret = {}

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
str = str.replace(',', '').replace('.', '')
str = str.split(' ')

indexes = [1,5,6,7,8,9,15,16,19]
for i in range(len(str)):
    if i + 1 in indexes:
        ret[i + 1] = str[i][0]
    else:
        ret[i + 1] = str[i][0:2]



print(ret)