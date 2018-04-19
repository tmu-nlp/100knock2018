import re
s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = re.findall(r'\w+', s)
pi_list = [len(w) for w in words]

print(pi_list)

# 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
# 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

# 実行結果
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
