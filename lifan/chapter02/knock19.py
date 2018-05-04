my_dict = {}
with open('hightemp.txt', 'r') as f:
	for line in f:
		word = line.split("\t")[0]
		if word in my_dict:
			my_dict[word] += 1
		else:
			my_dict[word] = 1

for k, v in sorted(my_dict.items(), key=lambda x: -x[1]):
    print(str(k) + ": " + str(v))
