import re

inputfile='jawiki.txt'
outputfile='jawiki-media.txt'

f=open(inputfile)
g=open(outputfile,'w')

mediafile=re.compile(r".*(ファイル|File|file):(.*\.[a-zA-Z0-9]+)\|.*")
for line in f:
	l=mediafile.match(line)
	if l:
		g.write(l.group(2)+"\n")

		