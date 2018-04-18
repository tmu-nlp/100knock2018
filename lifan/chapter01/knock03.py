import re
my_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.split(' |, ', my_string.rstrip("."))
print(words)
result = []
for word in words:
	result.append(len(word))
print(result)