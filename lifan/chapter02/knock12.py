with open('hightemp.txt', 'r') as f:
	with open('col1.txt', 'w') as wf1, open('col2.txt', "w") as wf2:
		for line in f:
			wf1.write(line.split("\t")[0]+"\n")
			wf2.write(line.split("\t")[1]+"\n")