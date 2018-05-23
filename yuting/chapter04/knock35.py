#35. 名詞の連接
#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

#三	名詞,数,*,*,*,*,三,サン,サン
#毛	名詞,接尾,助数詞,*,*,*,毛,モウ,モー
#君	名詞,接尾,人名,*,*,*,君,クン,クン三

#家族	名詞,一般,*,*,*,*,家族,カゾク,カゾク
#的	名詞,接尾,形容動詞語幹,*,*,*,的,テキ,テキ
#生活	名詞,サ変接続,*,*,*,*,生活,セイカツ,セイカツ
import knock30

def extract_seqs(sentences):
	seqs=[]
	seq=[]
	for sentence in sentences:
		for morpheme in sentence:
			if morpheme['pos']=="名詞":
				seq.append(morpheme['surface'])
			else:
				if len(seq)>1:
					seqs.append(seq)
				seq=[]
	return seqs
if __name__=='__main__':
	inputfile='neko.txt.mecab'
	outputfile='neko.mecab_sequence.txt'
	f=open(inputfile)
	g=open(outputfile,'w')
	sentences=knock30.mecab_reader(f)
	s=extract_seqs(sentences)
	for sequence in s:
		g.write("".join(sequence)+'\n')

	f.close()
	g.close()
	