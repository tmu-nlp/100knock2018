def create_char_n_gram(s, n):
    grams = []
    for i in range(len(s) - n + 1):
        grams.append(s[i:(i+n)])
    return grams


if __name__ == '__main__':
    s1 = 'paraparaparadise'
    s2 = 'paragraph'

    x = create_char_n_gram(s1, 2)
    y = create_char_n_gram(s2, 2)
    print(x)
    print(y)

    wa = x + y

    seki = []
    for w in wa:
        if (w in x) and (w in y):
            seki.append(w)
    
    sa = list(x)
    for w in x:
        if w in y:
            sa.remove(w)
    
    print('和集合: {0}'.format(wa))
    print('積集合: {0}'.format(seki))
    print('差集合: {0}'.format(sa))

    print(f"'se' in {s1} : " + str('se' in x))
    print(f"'se' in {s2} : " + str('se' in y))
