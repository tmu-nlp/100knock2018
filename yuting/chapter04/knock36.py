#36. 単語の出現頻度
#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import knock30
from collections import Counter

def count_word(sentences):
	words=[]
	
	for sentence in sentences:
		for morpheme in sentence:
			words.append(morpheme['surface'])
	return Counter(words)

if __name__=='__main__':
	inputfile='neko.txt.mecab'
	outputfile='neko.mecab_count.txt'
	f=open(inputfile)
	g=open(outputfile,'w')
	sentences=knock30.mecab_reader(f)
	counter=count_word(sentences)
	for word,count in counter.most_common():
		g.write("%s %s\n" %(word,count))

	f.close()
	g.close()
