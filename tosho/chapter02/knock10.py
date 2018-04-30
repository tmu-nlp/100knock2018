import argparse

# wc command
# http://tech.nikkeibp.co.jp/it/article/COLUMN/20060228/230994/

# equivalent (partial)
# wc hightemp.txt
#       24      98     813 hightemp.txt

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    lines = 0
    with open(arg.file, 'r') as f:
        for l in f:
            lines += 1
    
    print(lines)
