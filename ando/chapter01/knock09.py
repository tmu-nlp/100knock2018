import random

w = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
w = w.split(" ")
final = []
result=""
for i in range(len(w)):
    if len(w[i])<5:
        final.append(w[i])
        pass
    else:
        word = list(w[i])
        word2 = word[1:-1]
        random.shuffle(word2)
        word2.insert(0,word[0])
        word2.append(word[-1])
        word2 = ",".join(word2)
        final.append(word2.replace(",",""))
for i in final:
    result+=i+" "
print(result)