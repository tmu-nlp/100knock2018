# -*- coding: utf-8 -*-

x = 'I have a pen'

def cipher(sent):
    ret = ''
    for c in sent:
        if c.islower():
            ret += chr(219 - ord(c))
        else:
            ret += c
    print(ret)

cipher(x)