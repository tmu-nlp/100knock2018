import re
my_string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = re.split(' |\. ', my_string.rstrip("."))
print(words)
result = {}
for i in range(len(words)):
	if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
		result[i+1] = words[i][0]
	else:
		result[i+1] = words[i][:2]
print(result)