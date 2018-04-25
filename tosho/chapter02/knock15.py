import argparse
import sys

# python knock15.py -n N file
# select last N lines in given file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', type=int, default=10)
    parser.add_argument('file')

    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        remains = arg.n
        for line in f.read().splitlines()[::-1]:
            sys.stdout.write(line + '\n')
            remains -= 1
            if remains <= 0:
                break