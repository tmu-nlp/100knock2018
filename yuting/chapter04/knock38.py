#38. ヒストグラム
#単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け

import matplotlib.pyplot as plt
import knock36
import knock30
import pandas as pd

def plot_words_hist(freq,file):
	#Figure        图
	#Axes          坐标轴(实际画图的地方)
	fig=plt.figure()
	ax = fig.add_subplot(132)
	ax.hist(freq, bins=50, range=(0, 50))
	ax.set_title('Histogram of word count')
	ax.set_xlabel('Word count')
	ax.set_ylabel('Frequency')

if __name__=='__main__':
	inputfile='neko.txt.mecab'
	outputfile='neko.mecab_words_hist.png'
	f=open(inputfile,'r')
	

	sentences=knock30.mecab_reader(f)
	counter=knock36.count_word(sentences)

	
	
	freq=pd.Series(list(counter.values()),index=list(counter.keys()))
	plot_words_hist(freq,outputfile)


