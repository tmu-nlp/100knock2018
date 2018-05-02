import sys


def print_distinct(filename):
    '1列目の文字列の種類を表示する'
    lines = open(filename, encoding='utf-8').readlines()
    distinct_list = list(set(line.split()[0] for line in lines))
    print('\n'.join(distinct_list))


if __name__ == "__main__":
    fn = sys.argv[1]
    print_distinct(fn)


# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# Unix command
# cut hightemp.txt -f1 | sort | uniq

# 実行結果
# 高知県
# 愛媛県
# 山梨県
# 大阪府
# 埼玉県
# 静岡県
# 山形県
# 愛知県
# 岐阜県
# 和歌山県
# 群馬県
# 千葉県
