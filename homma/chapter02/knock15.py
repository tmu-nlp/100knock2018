import sys


def tail(filename, n):
    '末尾からN行を出力'
    # lines = open(filename, encoding='utf-8').readlines()
    # for line in lines[-n:]:
    #     print(line.strip())
    length = sum(1 for _ in open(filename, encoding='utf-8'))

    for i, line in enumerate(open(filename, encoding='utf-8')):
        if i >= length - n:
            yield line.strip()

    # return [line.strip() for i, line in enumerate(open(filename, encoding='utf-8')) if i >= length - n]


if __name__ == "__main__":
    fn = sys.argv[1]
    n = int(sys.argv[2])
    # tail(fn, n)
    for line in tail(fn, n):
        print(line)


# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

# Unix command
# tail hightemp.txt -n5

# 実行結果
# 埼玉県  鳩山    39.9    1997-07-05
# 大阪府  豊中    39.9    1994-08-08
# 山梨県  大月    39.9    1990-07-19
# 山形県  鶴岡    39.9    1978-08-03
# 愛知県  名古屋  39.9    1942-08-02
