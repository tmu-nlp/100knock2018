
ENWIKI_PATH = "enwiki.txt"
TOKENS_PATH = "tokens.txt"
tokens = []
with open(ENWIKI_PATH, "r") as fin, open(TOKENS_PATH, "w") as fout:
	for line in fin:
		words = line.strip().split()
		for w in words:
			w = w.strip('.,!?;:()[]\'\"')
			if len(w) > 0:
				tokens.append(w)

	fout.write(" ".join(tokens))