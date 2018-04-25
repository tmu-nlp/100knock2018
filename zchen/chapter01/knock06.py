from knock05 import n_gram

s1 = "paraparaparadise"
s2 = "paragraph"

bg1 = n_gram(2, s1)
bg2 = n_gram(2, s2)
se  = n_gram(2, "se")[0]

print("Union:", set(bg1) or set(bg2))
print("Intersection:", set(bg1) and set(bg2))
print("minus:", set(bg1) - set(bg2))
print(se, "in bigram(", s1, "):", se in bg1)
print(se, "in bigram(", s2, "):", se in bg2)
