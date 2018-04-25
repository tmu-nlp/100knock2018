# -*- coding: utf-8 -*-

str = "I am an NLPer"

def get_n_gram(seq, n):
    ret = []
    for i in range(len(seq)):
        item = ''
        count = 0
        for j in range(n):
            if i + j < len(seq):
                item += seq[i + j]
                count += 1
            else:
                continue
        if count == n:
            ret.append(item)
    return ret

in1 = str.replace(',', '').replace('.', '')
in1 = in1.split(' ')
print(get_n_gram(in1, 2))

in2 = str.replace(',', '').replace('.', '').replace(' ', '')
print(get_n_gram(in2, 2))
