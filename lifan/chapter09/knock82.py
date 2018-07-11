import random

TOKENS_CN_PATH = "tokens_cn.txt"
CONTEXT_PATH = "context.txt"

with open(TOKENS_CN_PATH, "r") as fin, open(CONTEXT_PATH, "w") as fout:
	tokens_arr = fin.read().split()
	for idx, t in enumerate(tokens_arr):
		if idx == 0 or len(tokens_arr) - idx == 1:
			d_width = 0
		elif idx < 5 or len(tokens_arr) - idx <= 5:
			d_width = random.choice(range(1, min(idx+1, len(tokens_arr) - idx)))
		else:
			d_width = random.choice(range(1, 6))
		pre_words = tokens_arr[idx-d_width:idx]
		sub_words = tokens_arr[idx+1:idx+d_width+1]
		c = " ".join(pre_words+sub_words)
		fout.write(f"{t}\t{c}\n")