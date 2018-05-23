#37. 頻度上位10語
#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ

import matplotlib.pyplot as plt
import knock36
import knock30
from collections import Counter
import numpy as np
from matplotlib.font_manager import FontProperties


def plot_words(word_list,frq_list,file):
	x=range(1,11)
	y=frq_list

	plt.bar(x,y)
	plt.xticks(x,word_list)
	plt.xlabel('WORD')
	plt.ylabel('COUNTS')
	plt.savefig(file)



if __name__=='__main__':
	inputfile = 'neko.txt.mecab'
	outputfile = 'neko.mecab_words.png'
	f = open(inputfile, 'r')
	g = open(outputfile,'w')

	word_list=[]
	frq_list=[]


	sentences=knock30.mecab_reader(f)
	counter=knock36.count_word(sentences)
	for word,count in counter.most_common(10):
		word_list.append(str(word))
		frq_list.append(int(count))
	
		
	plot_words(word_list,frq_list,outputfile)
	f.close()


#質問：横単語が出てこない。

#の 9194
#。 7486
#て 6868
#、 6772
#は 6420
#に 6243
#を 6071
#と 5508
#が 5337
#た 3988	
	















