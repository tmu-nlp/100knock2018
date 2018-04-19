import sys,random,itertools
sentence = "i couldn't control myself now beacause i am go to mad"
words = [word.strip(",.") for word in sentence.split()]
for idx,word in enumerate(words):
	ret = ""
	l = len(word)
	if 4<l:
		ret +=word[0]
		perm = list(itertools.permutations(list(word[1:l-1]),l-2))
		rnd = random.randint(0,len(perm)-1)
		ret +="".join(perm[rnd])
		ret +=word[l-1]
		words[idx]=ret

print(words)