import argparse
from collections import defaultdict

# sort command
# http://tech.nikkeibp.co.jp/it/article/COLUMN/20060227/230887/

# equivalent
# sort -k 1,1 -u hightemp.txt

# usage
# python knock18.py hightemp.txt -k 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-k', type=int, required=True)
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        lines = sorted(list(f.read().splitlines()))
    
    keys = []
    count = 0
    for line in lines:
        words = line.split('\t')
        key = words[arg.k - 1]

        if key not in keys:
            keys.append(key)
            count += 1
            
    print(count)

