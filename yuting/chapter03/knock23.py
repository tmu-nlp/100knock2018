import re

inputfile='jawiki.txt'
outputfile='jawiki-section.txt'

f=open(inputfile)
g=open(outputfile,'w')

section=re.compile(r'=(=+)(.+)=')

for line in f:
	l=section.match(line)
	if l:
		g.write("sec%s : "%len(l.group(1)))
		g.write(l.group(2) +"\n")

