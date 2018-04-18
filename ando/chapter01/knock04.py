genso = {}
w = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
w = re.sub('[,|.]',"",w)
w = w.split(" ")
numlist = [0, 4, 5, 6, 7, 8, 14, 15, 18]
for i in range(len(w)):
    if i in numlist:
        word = w[i]
        genso[word[0]] = i
    else:
        word = w[i]
        genso[word[0:2]] = i
print(genso)