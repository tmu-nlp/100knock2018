from utils import non_word

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
los = non_word.split(s)
print("".join(str(len(s)) for s in los))


