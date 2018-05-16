import argparse
import sys

# cut command
# http://tech.nikkeibp.co.jp/it/article/COLUMN/20060228/231159/

# equivalent
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt

# usage
# python knock11.py -f 1 2 -o col1.txt col2.txt

newline = '\n'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('-f', '--fields', action='store', type=int, nargs='+', required=True)
    parser.add_argument('-o', '--output', action='store', type=str, nargs='+', required=True)
    arg = parser.parse_args()

    if len(arg.fields) != len(arg.output):
        print('bad files or output length')
        sys.exit(1)

    # 入力は1起点なので、0起点に変換する
    fields = [(i - 1) for i in arg.fields]
    outputs = [open(o, 'w') for o in arg.output]
    n = len(arg.fields)

    with open(arg.file, 'r') as f:
        for line in f:
            words = line.strip().split('\t')    # stripは基本入れておいたほうがよい
            for i in range(n):
                outputs[i].write(words[fields[i]] + newline)