import sys

def line_count(filename):
    'ファイルの行数を数える'
    return len(open(filename, encoding='utf-8').readlines())


if __name__ == "__main__":
    fn = sys.argv[1]
    print(line_count(fn))

# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# Unix command
# cat hightemp.txt | wc -l

# 実行結果
# 24
