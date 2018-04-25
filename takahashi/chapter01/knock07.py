# -*- coding: utf-8 -*-

x = 12
y = '気温'
z = 22.4

def show_me_sentence(x, y, z):
    ret = str(x) + '時の' + str(y) + 'は' + str(z)
    print(ret)

show_me_sentence(x, y, z)