from random import shuffle
setence="i couldn't control mysel now"
def typo(word):
	middle=list(word[1:-1])
	shuffle(middle)
	return word[0]+''.join(middle)+word[-1]

print(''.join(typo(w) if len(w)>4 else w for w in setence.split()))