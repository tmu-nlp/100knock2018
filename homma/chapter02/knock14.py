import sys


def head(filename, n):
    '先頭からN行を出力'
    # lines = open(filename, encoding='utf-8').readlines()
    # for line in lines[:n]:
    #     print(line.strip())
    for line, _ in zip(open(filename, encoding='utf-8'), range(n)):
        yield line.strip()


if __name__ == "__main__":
    fn = sys.argv[1]
    n = int(sys.argv[2])
    # head(fn, n)
    for line in head(fn, n):
        print(line)


# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

# Unix command
# head hightemp.txt -n5

# 実行結果
# python knock14.py hightemp.txt 5
# 高知県  江川崎  41      2013-08-12
# 埼玉県  熊谷    40.9    2007-08-16
# 岐阜県  多治見  40.9    2007-08-16
# 山形県  山形    40.8    1933-07-25
# 山梨県  甲府    40.7    2013-08-10
