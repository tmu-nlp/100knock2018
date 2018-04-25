import argparse

newline = '\n'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    arg = parser.parse_args()

    with open(arg.file, 'r') as f:
        with open('col1.txt', 'w') as c1:
            with open('col2.txt', 'w') as c2:
                for line in f:
                    words = line.split('\t')
                    c1.write(words[0] + newline)
                    c2.write(words[1] + newline)

# cut コマンド
# http://www.atmarkit.co.jp/ait/articles/1610/31/news026.html
# equals to following cmds:
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt