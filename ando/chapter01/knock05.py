def gram(wlist):
    backlist = []
    for i in range(len(wlist)):
        if i == len(wlist)-1:
            return backlist
        backlist.append(wlist[i]+"-"+wlist[i+1])
w = "I am an NLPer"
w1 = w.split(" ")
w = w.replace(" ","")
w2 = list(w)
print(gram(w1),gram(w2))