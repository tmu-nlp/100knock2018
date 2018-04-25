def create_n_gram(s, n):
    s = s.replace(',', ' ,')
    s = s.replace('.', ' .')

    words = s.split(' ')
    grams = []
    for i in range(len(words) - n + 1):
        grams.append(words[i:(i+n)])
    return grams

if __name__ == '__main__':
    s = 'I am a NLPer'
    grams = create_n_gram(s, 2)
    print(grams)