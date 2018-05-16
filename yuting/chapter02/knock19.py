#import itemgetter

with open('hightemp.txt','r',encoding='utf-8')as file_temp:
	text=file_temp.read()

col1=[]
col2=[]
for line in text.split('\n'):
	col1.append(line.split('\t')[0])

col1.sort()
for value in set(col1):
	if value !='':
		col2.append([col1.count(value)]+[value])

col2.sort(key=lambda x:x[0])
col2.reverse()

for value in col2:
	print(value)