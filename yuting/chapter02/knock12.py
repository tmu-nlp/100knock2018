file_temp=open('hightemp.txt','r',encoding='utf-8')
text=file_temp.read()
file_temp.close()

lst_col1=[]
lst_col2=[]
for line in text.split('\n'):
	if len(line)>0:
		lst_col1.append(line.split('\t')[0])
		lst_col2.append(line.split('\t')[1])

file_col1=open('col1.txt','a',encoding='utf-8')
file_col2=open('col2.txt','a',encoding='utf-8')

print(*lst_col1,sep='\n',file=file_col1)
print(*lst_col2,sep='\n',file=file_col2)

file_col1.close()
file_col2.close()