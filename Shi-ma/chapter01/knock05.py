def ngram(string, n):
    return list(zip(*[string[i:] for i in range(n)]))

if __name__ == '__main__':
    string = 'I am an NLPer'
    print(ngram(string.strip().split(), 2))
    print(ngram(string.replace(' ', '_'), 2))
