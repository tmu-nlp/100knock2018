str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
ans = [len(word.strip(",.")) for word in str.split()]

print(ans)

