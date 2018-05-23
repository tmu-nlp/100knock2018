import re


inputfile='jawiki-catogray.txt'
outputfile='jawiki-catogray-name.txt'

f=open(inputfile)
g=open(outputfile,'w')

category=re.compile('\[\[Category:(.+)\]\]')

for line in f:
	l=category.match(line)
	if l:
		g.write(l.group(1) + "\n")