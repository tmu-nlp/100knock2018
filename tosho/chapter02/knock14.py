import argparse
import sys

# python knock14.py -n N file
# select first N lines in given file

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', action='store', type=int, default=10)
    parser.add_argument('file')

    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        remains = arg.n
        for line in f:
            sys.stdout.write(line)
            remains -= 1
            if remains <= 0:
                break