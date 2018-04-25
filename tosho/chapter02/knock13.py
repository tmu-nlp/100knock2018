import argparse

# paste command
# http://tech.nikkeibp.co.jp/it/article/COLUMN/20131209/523511/

# equivalent
# paste col1.txt col.txt > col1_2.txt

# usage
# python knock13.py col1.txt col2.txt -o col1_2.txt

newline = '\n'
tab = '\t'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file1')
    parser.add_argument('file2')
    parser.add_argument('-o', '--output', action='store', type=str, required=True)
    arg = parser.parse_args()

    with open(arg.file1, 'r') as i1:
        with open(arg.file2, 'r') as i2:
            lines = zip(
                i1.read().splitlines(),
                i2.read().splitlines()
            )

            with open(arg.output, 'w') as o:
                for line in lines:
                    o.write(line[0] + tab + line[1] + newline)
