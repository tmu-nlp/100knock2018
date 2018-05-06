import sys


def merge_columns_and_write(infile1, infile2, outfile):
    '2つのファイルを列で結合して保存する'
    col1 = open(infile1, encoding='utf-8').readlines()
    col2 = open(infile2, encoding='utf-8').readlines()
    with open(outfile, mode='w', encoding='utf-8') as f:
        f.writelines(f'{c1.strip()}\t{c2.strip()}\n' for c1, c2 in zip(col1, col2))


if __name__ == "__main__":
    fn1 = sys.argv[1]
    fn2 = sys.argv[2]
    out = sys.argv[3]
    merge_columns_and_write(fn1, fn2, out)


# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

# Unix command
# paste col1.txt col2.txt

# 実行結果
