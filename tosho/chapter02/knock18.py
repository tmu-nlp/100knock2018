import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        lines = sorted(f, 
            key=lambda line: float(line.split('\t')[2]),
            reverse=True
        )

    for line in lines:
        sys.stdout.write(line)