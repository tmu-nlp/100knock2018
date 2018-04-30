with open('col1.txt', 'r') as col1, open('col2.txt', 'r') as col2, open('col1col2.txt', 'w') as col12:
	for (line1,line2) in zip(col1,col2):
		col12.write("{}\t{}".format(line1.strip(), line2))