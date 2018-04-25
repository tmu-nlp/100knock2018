sentence = "now i need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
count = [len(word.strip(".,")) for word in sentence.split()]
print(count)
