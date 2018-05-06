import sys


def separate_columns_and_write_separately(filename):
    'ファイルの1列目と2列目を別々のファイルに保存'
    lines = open(filename, encoding='utf-8').readlines()
    with open('col1.txt', mode='w', encoding='utf-8') as f:
        f.writelines(f'{line.split()[0]}\n' for line in lines)
    with open('col2.txt', mode='w', encoding='utf-8') as f:
        f.writelines(f'{line.split()[1]}\n' for line in lines)


if __name__ == "__main__":
    fn = sys.argv[1]
    separate_columns_and_write_separately(fn)

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

# Unix command
# cut hightemp.txt -f1
# cut hightemp.txt -f2

# 実行結果
