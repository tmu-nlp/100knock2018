# tail -n N '../data/hightemp.txt'

import argparse



def tail(path, N):
    length = sum([1 for line in open(path)])

    for i, line in enumerate(open(path)):
        if i >= (length - N):
            yield line.strip()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, default=10)
    parser.add_argument('path')

    args = parser.parse_args()

    for line in tail(args.path, args.n):
        print(line)
