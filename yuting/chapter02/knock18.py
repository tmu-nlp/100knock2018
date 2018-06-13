with open('hightemp.txt','r',encoding='utf-8')as file_temp:
	lines=file_temp.readlines()

lines2=[]
for line in lines:
	lines2.append(line.split('\t'))

key_temp=lambda x:float(x[2])

for line in sorted(lines2,key=key_temp,reverse=True):
	print('\t'.join(line),end='')