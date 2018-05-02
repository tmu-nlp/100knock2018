my_list = []
with open('hightemp.txt', 'r') as f:
	for line in f:
		my_list.append(line.split("\t")[2])
my_list.sort()
my_list.reverse()
print(my_list)