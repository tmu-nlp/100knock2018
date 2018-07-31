import random


def main():
    f_pos = open('rt-polarity.pos', encoding='cp1252')
    f_neg = open('rt-polarity.neg', encoding='cp1252')
    lines = [f'+1 {l}' for l in f_pos] + [f'-1 {l}' for l in f_neg]
    random.shuffle(lines)

    with open('sentiment.txt', 'w', encoding='cp1252') as f:
        f.writelines(lines)


if __name__ == '__main__':
    main()


''' 問
70. データの入手・整形

文に関する極性分析の正解データを用い，
以下の要領で正解データ（sentiment.txt）を作成せよ．

1. rt-polarity.posの各行の先頭に"+1 "という文字列を追加する
  （極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
2. rt-polarity.negの各行の先頭に"-1 "という文字列を追加する
  （極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
3. 上述1と2の内容を結合（concatenate）し，行をランダムに並び替える

sentiment.txtを作成したら，正例（肯定的な文）の数と
負例（否定的な文）の数を確認せよ．
'''

''' 実行結果
$ grep -e +1 sentiment.txt | wc -l
5331

$ grep -e ^-1 sentiment.txt | wc -l
5331
'''
