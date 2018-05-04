# sort -k3　-n ../data/hightemp.txt

if __name__ == '__main__':
    path = '../data/hightemp.txt'

    print('\n'.join(sorted([line.strip() for line in open(path)], key=lambda x: x.strip().split()[2], reverse=True)))
