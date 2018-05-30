import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import math
from util import *


words,sentence = yomikomi()
hindo={}
value=[]
key=[]
hindo2={}
for j in sentence:
    for i in j:
        word=i["surface"]
        if word not in hindo:
            hindo[word] = 1
        else:
            hindo[word] += 1
sort = sorted(hindo.items(), key=lambda x: x[1], reverse = True)
for i in range(len(sort)):
    if sort[i][1] not in hindo2:
        hindo2[sort[i][1]]=1
    else:
        hindo2[sort[i][1]]+=1
sort = sorted(hindo2.items(), key=lambda x: x[0], reverse = True)
for i in range(len(sort)):
    key.append(math.log(sort[i][0]))
    value.append(math.log(sort[i][1]))
plt.plot(key,value)
plt.savefig('figure.png')