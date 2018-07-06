'''
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
'''
import random

sentiment = []

# posのラベル付け
for line in open('rt-polaritydata/rt-polarity.pos', 'r', encoding='latin-1'):
    sentiment.append(f'+1 {line}')

# negのラベル付け
for line in open('rt-polaritydata/rt-polarity.neg', 'r', encoding='latin-1'):
    sentiment.append(f'-1 {line}')

# シャッフル
random.shuffle(sentiment)

# concatenate
with open('sentiment.txt', 'w') as f:
    for line in sentiment:
        f.write(line)

# posとnegの数を確認
pos = 0
neg = 0
for line in open('sentiment.txt', 'r'):
    if line[0] == '+':
        pos += 1
    elif line[0] == '-':
        neg += 1

print(f'pos: {pos}')
print(f'neg: {neg}')
