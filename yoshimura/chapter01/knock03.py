str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

list = []
for word in str.split(" "):
    list.append(len(word.strip(".,")))

print(list)