# paste ../data/col1.txt ../data/col2.txt

def marge(symbol, *paths):
    for col_list in zip(*map(lambda path: open(path), paths)):
        yield '\t'.join(map(lambda col: col.strip(), col_list))



if __name__ == '__main__':
    path1 = '../data/col1.txt'
    path2 = '../data/col2.txt'

    with open('../data/col3.txt', 'w') as marge_out:
        for line in marge('\t', path1, path2):
            marge_out.write(line + '\n')
