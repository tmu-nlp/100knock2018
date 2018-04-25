import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        for line in f:
            o = line.replace('\t', ' ')
            sys.stdout.write(o)

# equals to 'expand -t 1'