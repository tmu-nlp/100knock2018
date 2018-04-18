import re
import random
my_string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
words = re.split(' ', my_string.rstrip(" .").replace(": ", ""))
print(words)
for i in range(len(words)):
	if len(words[i]) >= 4:
		middle_list = list(words[i][1:-1])
		random.shuffle(middle_list)
		words[i] = words[i][0] + "".join(middle_list) + words[i][-1]
print(words)