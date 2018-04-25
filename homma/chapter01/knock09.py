import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
res = []
for w in s.split(' '):
    if len(w) > 4:
        w = w[0] + ''.join(random.sample(w[1:-1], len(w) - 2)) + w[-1]
    res.append(w)
res = ' '.join(res)


print(res)

# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
# を与え，その実行結果を確認せよ．

# 実行結果
# I cn'duolt biveele that I could aalcltuy ueatnsdnrd what I was rdinaeg : the paoennmehl power of the human mind .

# 闇（ワンライナー）
# import random; print(' '.join(w if len(w) <= 4 else w[0] + ''.join(random.sample(w[1:-1], len(w) - 2)) + w[-1] for w in s.split(' ')))