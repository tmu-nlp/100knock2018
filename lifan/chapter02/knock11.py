with open('hightemp.txt', 'r') as f:
	for line in f:
		line = line.replace('\t', ' ')
		print(line, end="")