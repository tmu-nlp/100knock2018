#33. サ変名詞
#サ変接続の名詞をすべて抽出せよ．

import knock30

def extract_san(sentences):
	res=[]
	for sentence in sentences:
		for morpheme in sentence:
			if morpheme['pos']=='名詞' and morpheme['pos1']=='サ変接続':#完全一致必要がある
					res.append(morpheme['surface'])
	return res

if __name__=='__main__':
	inputfile='neko.txt.mecab'
	outputfile='neko.mecab_san.txt'
	f=open(inputfile,'r')
	g=open(outputfile,'w')
	sentences=knock30.mecab_reader(f)
	res=extract_san(sentences)
	for s in res:
		g.write(s+'\n')

	f.close()
	g.close()
