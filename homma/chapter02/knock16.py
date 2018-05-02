import sys
from more_itertools import chunked

def split(filename, n):
    'ファイルをN行ずつに分割'
    lines = open(filename, encoding='utf-8').readlines()
    chunks = chunked(lines, n)
    for i, chunk in enumerate(chunks):
        with open(f'{filename}_splited{i:02}', mode='w', encoding='utf-8') as f:
            f.writelines(f'{line}' for line in chunk)


if __name__ == "__main__":
    fn = sys.argv[1]
    n = int(sys.argv[2])
    split(fn, n)


# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

# Unix command
# split -l5 hightemp.txt

# 実行結果
# 埼玉県  鳩山    39.9    1997-07-05
# 大阪府  豊中    39.9    1994-08-08
# 山梨県  大月    39.9    1990-07-19
# 山形県  鶴岡    39.9    1978-08-03
# 愛知県  名古屋  39.9    1942-08-02
