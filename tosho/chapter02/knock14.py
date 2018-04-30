import argparse

# head command
# http://tech.nikkeibp.co.jp/it/article/COLUMN/20060227/230794/

# equivalent
# head -n 10 hightemp.txt

# usage
# python knock14.py -n 10 hightemp.txt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', type=int, default=10)
    parser.add_argument('file')

    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        for line in f.read().splitlines()[:arg.n]:
            print(line)