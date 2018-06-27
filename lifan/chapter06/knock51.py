import re

pattern = re.compile(r'[,.;:?!"()]')
with open('50_output.txt', 'r') as fin, open('51_output.txt', 'w') as fout:
	for line in fin:
		for word in line.split(' '):
			word = pattern.sub('', word)
			fout.write(f"{word}\n")