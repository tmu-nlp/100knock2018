# head -n N '../data/hightemp.txt'

import sys



def head(path, N):
    for line, i in zip(open(path), range(N)):
        yield line.strip()



if __name__ == '__main__':
    N = int(sys.argv[1])

    path = '../data/hightemp.txt'

    for line in head(path, N):
        print(line)
