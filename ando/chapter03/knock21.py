line = open("igirisu.txt").readlines()
for i in line:
	if "[[Category:" in i:
		print(i)