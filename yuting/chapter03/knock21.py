import re

inputfile=('jawiki.txt')
outputfile=('jawiki-catogray.txt')

f=open(inputfile)
g=open(outputfile,'w')

category=re.compile('\[\[Category:.+\]\]')

for line in f:
	if category.match(line):
		g.write(line.strip() + "\n")

f.close()
g.close()



#[[Category:イギリス|*]]
#[[Category:英連邦王国|*]]
#[[Category:G8加盟国]]
#[[Category:欧州連合加盟国]]
#[[Category:海洋国家]]
#[[Category:君主国]]
#[[Category:島国|くれいとふりてん]]
#[[Category:1801年に設立された州・地域]]
