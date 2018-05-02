word1 = "paraparaparadise"
word2 = "paragraph"
x = set([word1[i:i+2] for i in range(len(word1)-1)])
y = set([word2[i:i+2] for i in range(len(word2)-1)])

print("x=" + str(x))
print("y=" + str(y))
print(str(x|y))
print(str(x-y))
print(str(x&y))

if 'se' in x:
	print("include x")
if 'se' in y:
	print("include y")
