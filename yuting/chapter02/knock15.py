print('input a number n = ',end='')

input_number=input()
input_number=int(input_number)

with open('hightemp.txt','r',encoding='utf-8')as input_data:
	lines=input_data.readlines()

for line in lines[-input_number:]:
	print(line,end='')


#input a number n = 3
#山梨県	大月	39.9	1990-07-19
#山形県	鶴岡	39.9	1978-08-03
#愛知県	名古屋	39.9	1942-08-02