my_set = set()
with open('hightemp.txt', 'r') as f:
	for line in f:
		my_set.add(line.split("\t")[0])
my_list = list(my_set)
my_list.sort()
print(my_list)