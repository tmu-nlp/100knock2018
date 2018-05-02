with open('col1.txt','r',encoding='utf-8')as col1_temp,open ('col2.txt','r',encoding='utf-8')as col2_temp,open('col1and2.txt','a',encoding='utf-8')as file_col1and2:
	col1and2=''
	for col1,col2 in zip(col1_temp.read().split('\n'),col2_temp.read().split('\n')):
		col1and2 +=col1+'\t'+col2+'\n'

	print(col1and2,file=file_col1and2)