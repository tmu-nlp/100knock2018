import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

words = []
for w in s.split():
    if len(w) > 4:
        l = list(w[1:-1])
        random.shuffle(l)
        l = "".join(l)
        w = w[0] + l + w[-1]
    words.append(w)

ans = ' '.join(words)

print(ans)
