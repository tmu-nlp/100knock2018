# -*- coding: utf-8 -*-

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str = str.replace(',', '').replace('.', '')
ret = str.split(' ')
print(ret)