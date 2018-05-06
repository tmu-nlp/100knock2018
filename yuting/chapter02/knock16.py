print('cut in number n=',end='')
input_num=input()
input_num=int(input_num)

with open('hightemp.txt',encoding='utf-8')as input_data:
	lines=input_data.readlines()
	lines_size=len(lines)

	unit_size=lines_size // input_num
	res=lines_size % input_num

	indeces=[0]
	for i in range(1,input_num):
		indeces.append(indeces[-1]+unit_size)
		if res >0:
			indeces[-1] +=1
			res -=1
	indeces.append(lines_size)
	

for i in range(len(indeces)-1):
	with open('hightemp_split_'+str(i)+'.txt','w',encoding='utf-8')as output_data:
		output_data.writelines(lines[indeces[i]:indeces[i+1]])