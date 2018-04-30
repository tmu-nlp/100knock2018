sentence ="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
words = [word.strip(",.") for word in sentence.split()]

link = {}
for i,v in enumerate(words,1):
	length = 1 if i in [1,5,6,7,8,9,15,16,19] else 2
	link.update({v[:length]:i})
print(link)
