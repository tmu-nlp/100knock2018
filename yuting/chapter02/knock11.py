file_temp=open('hightemp.txt','r',encoding='utf-8')
text=file_temp.read()
file_temp.close()
print(text.replace('\t',' '))
