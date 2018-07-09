# -*- coding: utf-8 -
import random


def read_polarity():
    lines=[]

    for line in open('rt-polarity.pos','r',encoding='latin-1'):
        lines.append('+1'+line)

    for line in open('rt-polarity.neg','r',encoding='latin-1'):
        lines.append('-1'+line)

    random.shuffle(lines)
    return lines
def write_sentiment(lines):
    f=open('sentiment.txt','w')
    for line in lines:
        f.write(line)
    f.close()


write_sentiment(read_polarity())

