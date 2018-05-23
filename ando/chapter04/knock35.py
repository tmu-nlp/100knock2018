sentence=[]
kari={}
words=[]

befor1=""
befor2=""
hinsi=""
hinsi2=""
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
best = ""
bestnum = 0
for j in sentence:
    for i in range(len(j)):
        bestkouho = ""
        for v in range(len(j)):
            try:
                before1=j[i+v]["surface"]
                hinsi1=j[i+v]["pos"]
                hinsi=j[i]["pos"]
                if hinsi == "名詞" and hinsi1 == "名詞":
                    bestkouho += j[i+v]["surface"]
                    if bestnum < len(bestkouho):
                        best = bestkouho
                        bestnum = len(bestkouho)
                        print(best)
                else:
                    break
            except:
                break
print(best)