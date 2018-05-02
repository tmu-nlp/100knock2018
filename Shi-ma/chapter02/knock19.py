# cut -f 1 ../data/hightemp.txt | sort | uniq -c | sort -nr

import collections



if __name__ == '__main__':
    path = '../data/col1.txt'
    col_dict = collections.defaultdict(int)

    for line in open(path):
        col_dict[line.strip()] += 1

    for key, value in sorted(col_dict.items(), key=lambda x: x[1], reverse=True):
        print(key, value)
