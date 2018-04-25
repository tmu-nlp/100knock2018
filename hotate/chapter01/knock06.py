def n_gram(n, words):
    n_gram = []
    for i in range(0, len(words)-1):
        n_gram.append(words[i:i+n])

    return n_gram

x = set(n_gram(2, "paraparaparadise"))
y = set(n_gram(2, "paragraph"))

union = x.union(y)
intersection = x.intersection(y)
difference = x.difference(y)

print(f'和集合：{union}\n差集合：{intersection}\n積集合：{difference}')

print('se' in x)
print('se' in y)

