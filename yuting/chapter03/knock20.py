import json


inputfile='jawiki-country.json'
outputfile='jawiki.txt'

f=open(inputfile)
g=open(outputfile,'w')

article_json=f.readline()
while article_json:
	article_dict=json.loads(article_json)
	if article_dict["title"]=="イギリス":
		g.write(article_dict["text"])
	article_json=f.readline()










#with open("jawiki-country.json") as f:
	#article_json=f.readline()
	#while article_json:
		#article_dict=json.loads(article_json)
		#if article_dict["title"] == u"イギリス":
			#print(article_dict["text"])
		#article_json=f.readline()





