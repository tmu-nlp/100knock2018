import argparse
import sys

# equivalent
# sort -k 3,3 -r hightemp.txt

# usage
# python knock18.py hightemp.txt -k 3

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-k', type=int, required=True)
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        lines = sorted(f, 
            key=lambda line: float(line.split('\t')[arg.k - 1]),
            reverse=True
        )

    for line in lines:
        sys.stdout.write(line)