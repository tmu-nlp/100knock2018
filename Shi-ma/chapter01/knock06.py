def ngram(string, n):
    return list(zip(*[string[i:] for i in range(n)]))


if __name__ == '__main__':
    txt01 = 'paraparaparadise'
    txt02 = 'paragraph'

    X = set(ngram(txt01, 2))
    Y = set(ngram(txt02, 2))

    print('X + Y = {}'.format(X | Y))
    print('X & Y = {}'.format(X & Y))
    print('X - Y = {}'.format(X - Y))
    print('Y - X = {}'.format(Y - X))
    print('\'se\' in X = {}'.format(bool(('s', 'e') in X)))
    print('\'se\' in Y = {}'.format(bool(('s', 'e') in Y)))
