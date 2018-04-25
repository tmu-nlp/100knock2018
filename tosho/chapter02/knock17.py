import argparse
from collections import defaultdict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        words = list(map(lambda line: line.split('\t')[0], f))

    ret = defaultdict(lambda : 0)
    for word in words:
        ret[word] += 1
    
    for word, count in ret.items():
        print(f'{word}')
    
    print('----------')
    print(f'{len(ret)} words')
