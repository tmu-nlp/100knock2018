def n_gram(n, words):
    n_gram = []
    for i in range(0, len(words)-1):
        n_gram.append(words[i:i+n])

    return n_gram

w = "I am an NLPer"
print("文字bi-gram : {}".format(n_gram(2, w)))
w=w.split()
print("単語bi-gram : {}".format(n_gram(2, w)))

