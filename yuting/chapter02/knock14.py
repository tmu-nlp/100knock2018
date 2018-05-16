print('自然数をひとつ入力してください。N = ',end='')
input_num = input()
input_num = int(input_num)

with open('hightemp.txt', encoding='utf-8') as input_data :
    lines = input_data.readlines()

for line in lines[ : input_num] :
    print(line,end='')