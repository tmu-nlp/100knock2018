import re
import json
import knock25 


def remove_emphasis(string):
	emphasis=re.compile(r"''('*)(.+)''\1")
	return emphasis.sub(r"\2",string)

if __name__=="__main__":
	inputfile='jawiki.txt'
	outputfile='jswiki-markup.json'
	f=open(inputfile)
	res=knock25.fundamental_data(f,remove_emphasis)
	with open(outputfile,'w')as g:
		json.dump(res,g,ensure_ascii=False)