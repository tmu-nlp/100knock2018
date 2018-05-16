# cat ../data/col1.txt | sort | uniq; sort ../data/col1.txt | uniq | wc -l

if __name__ == '__main__':
    print(len(set([line.strip() for line in open('../data/col1.txt')])))
