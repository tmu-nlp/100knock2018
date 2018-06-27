from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
with open('51_output.txt', 'r') as fin, open('52_output.txt', 'w') as fout:
	for word in fin:
		word = word.strip()
		fout.write(f"{word}\t{ps.stem(word)}\n")