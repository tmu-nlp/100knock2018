import argparse
import sys

# expand command
# http://tech.nikkeibp.co.jp/it/article/COLUMN/20131007/509542/

# equivalent
# expand -t 1 hightemp.txt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        for line in f:
            o = line.replace('\t', ' ')
            sys.stdout.write(o)
