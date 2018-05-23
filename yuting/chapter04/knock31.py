#動詞の表層形をすべて抽出せよ

import knock30

def extract_verb(sentences):
	res=[]
	for sentence in sentences:
		for morpheme in sentence:
			if morpheme['pos']=='動詞':#morpheme is 語素
				res.append(morpheme['surface'])
	return res

if __name__=="__main__":
	inputfile='neko.txt.mecab'
	outputfile='neko.mecab_verb.txt'
	f=open(inputfile,'r')
	g=open(outputfile,'w')
	sentences=knock30.mecab_reader(f)
	verbs=extract_verb(sentences)
	for verb in verbs:
		g.write(str(verb) +'\n')

	f.close()
	g.close()
	