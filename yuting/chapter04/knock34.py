#34. 「AのB」
#2つの名詞が「の」で連結されている名詞句を抽出せよ

#彼	名詞,代名詞,一般,*,*,*,彼,カレ,カレ
#の	助詞,連体化,*,*,*,*,の,ノ,ノ
#掌	名詞,一般,*,*,*,*,掌,テノヒラ,テノヒラ

import knock30

def extract_aofb(sentences):
	res=[]
	for sentence in sentences:
		for k in range(len(sentence)-3):
			triple=sentence[k:k+3]
			b1=triple[0]['pos']=='名詞'
			b2=triple[1]['surface']=='の'
			b3=triple[2]['pos']=='名詞'
			if b1 and b2 and b3:
				res.append(t['surface'] for t in triple)
	return res

if __name__=='__main__':
	inputfile='neko.txt.mecab'
	outputfile='neko.mecab_aofb.txt'
	f=open(inputfile)
	g=open(outputfile,'w')
	sentences=knock30.mecab_reader(f)
	res=extract_aofb(sentences)
	for r in res:
		g.write("".join(r)+'\n')

	f.close()
	g.close()