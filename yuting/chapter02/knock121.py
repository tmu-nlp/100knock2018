with open('hightemp.txt','r',encoding='utf-8')as original,\
    open('col1.txt','w',encoding='utf-8')as col1,\
    open('col2.txt','w',encoding='utf-8')as col2:

    for row in original.readlines():
    	row_split=row.split('\t')
    	col1.write(row_split[0]+'\n')
    	col2.write(row_split[1]+'\n')