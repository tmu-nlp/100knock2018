f = open("/Users/one/Downloads/hightemp.txt").read()
rep = f.replace("\t"," ")
with open("hightemp2.txt", "w") as fout:
	fout.write(rep)
"""
cat hightemp.txt | sed s/\t/ /g
"""