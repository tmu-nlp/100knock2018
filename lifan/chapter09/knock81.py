TOKENS_PATH = "tokens.txt"
COUNTRY_PATH = "country_names.txt"
TOKENS_CN_PATH = "tokens_cn.txt"

with open(TOKENS_PATH, "r") as ftoken, open(COUNTRY_PATH, "r") as fcountry, open(TOKENS_CN_PATH, "w") as fout:
	tokens_str = ftoken.read()
	country_arr = fcountry.read().split("\n")
	for c in country_arr:
		c_words = c.split()
		if len(c_words) > 1:
			tokens_str = tokens_str.replace(c, "_".join(c_words))
			#print("_".join(c_words))
	fout.write(tokens_str)