import sys
from collections import defaultdict


def sort_by_appearance(filename, n):
    'n列目を重複削除し，出現頻度の降順で並び替える'
    dic = defaultdict(lambda: 0)
    lines = open(filename, encoding='utf-8').readlines()
    for line in lines:
        dic[line.split()[n - 1]] += 1
    sorted_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print('\n'.join(t[0] for t in sorted_list))


if __name__ == "__main__":
    fn = sys.argv[1]
    sort_by_appearance(fn, 1)


# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

# Unix command
# cut -f1 hightemp.txt | sort | uniq -c | sort -nr

# 実行結果
# 埼玉県
# 山形県
# 山梨県
# 群馬県
# 岐阜県
# 静岡県
# 愛知県
# 千葉県
# 高知県
# 和歌山県
# 愛媛県
# 大阪府
