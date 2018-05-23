import matplotlib.pyplot as plt
import numpy as np
import matplotlib

sentence=[]
kari={}
words=[]


lines = open("neko_m.txt").readlines()
for line in lines:
  kari={}
  if "EOS" in line:
    break
  line= line.split("\t")
  line2=line[1].split(",")
  line.pop()
  line.extend(line2)
  if "。" in line[0]:
    sentence.append(words)
    words=[]
  kari["surface"]=line[0]
  kari["pos"]=line[1]
  kari["pos1"]=line[2]
  kari["base"]=line[7]
  words.append(kari)

hindo={}
value=[]
key=[]
for j in sentence:
    for i in j:
        word=i["surface"]
        if word not in hindo:
            hindo[word] = 1
        else:
            hindo[word] += 1
sort = sorted(hindo.items(), key=lambda x: x[1], reverse = True)

for i in range(10):
    key.append(sort[i][0])
    value.append(sort[i][1])
plt.plot(key,value)
plt.savefig('figure.png')