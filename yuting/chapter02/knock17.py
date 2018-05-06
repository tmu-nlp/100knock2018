with open('hightemp.txt','r',encoding='utf-8')as file_temp:
    text=file_temp.read()

lst_col1=[]
for line in text.split('\n'):
    lst_col1.append(line.split('\t')[0])

lst_col1.sort()
for value in lst_col1:
    if lst_col1.count(value)>1:
    	lst_col1.remove(value)

for value in lst_col1:
    print(value)