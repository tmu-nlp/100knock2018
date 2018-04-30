line_count = 0
with open('hightemp.txt', 'r') as f:
	for line in f:
		line_count += 1

print(line_count)