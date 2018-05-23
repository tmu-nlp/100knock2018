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
for j in sentence:
    count=1
    for i in range(len(j)):
        try:
            before1=j[i-1]["surface"]
            before2=j[i-2]["surface"]
            hinsi=j[i]["pos"]
            hinsi2=j[i-2]["pos"]
            if hinsi == "名詞" and hinsi2 == "名詞":
                if before1 == "の":
                    print(before2 + before1 + j[i]["surface"])
        except:
            continue