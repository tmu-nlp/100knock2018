def n_gram(n, s):
    ns = []
    for i in range(n):
        ns.append(s[i:])
    return tuple(zip(*ns))

if __name__ == "__main__":
    print(n_gram(2, "I am an NLPer"))
