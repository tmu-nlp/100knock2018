def load_countries(compound_only):
    with open('countries') as fr:
        for line in fr:
            if compound_only:
                if ' ' in line:
                    yield line.rstrip().split()
            else:
                yield line.rstrip()

def make_trie(compound_list):
    trie = {}
    for seq in compound_list:
        tr = trie
        for t in seq:
            if t not in tr:
                tr[t] = {}
            tr = tr[t]
    return trie

def combine_compound(line, trie, concat_sign = '_'):
    i = 0
    new_line = []
    max_len = len(line)
    while i < max_len:
        tr = trie
        j = i
        while line[j] in tr:
            tr = tr[line[j]]
            j += 1
            if j == max_len:
                j = i
                break
        if i != j and tr == {}:
            new_line.append(concat_sign.join(line[i:j]))
            i = j
        else:
            new_line.append(line[i])
            i += 1
    return new_line

def test():
    compound_list = list(load_countries(True))
    trie = make_trie(compound_list)
    line = 'North Korea and South Korea were once one country South Africa and South Sudan were ever not'.split()
    print(combine_compound(line, trie))

if __name__ == '__main__':
    import cProfile
    cProfile.run('test()')
