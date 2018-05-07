import argparse
from collections import defaultdict

# equivalent
# cut -f 1 hightemp.txt | sort | uniq -c | sort -k 1 -r

# usage
# python knock19.py hightemp.txt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        words = list(map(lambda line: line.split('\t')[0], f))

    ret = defaultdict(lambda : 0)
    for word in words:
        ret[word] += 1
    
    for word, count in sorted(ret.items(), key=lambda item: item[1], reverse=True):
        print(f'{count} {word}')


    