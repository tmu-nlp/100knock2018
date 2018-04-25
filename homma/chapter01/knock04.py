import re
s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
one = [1, 5, 6, 7, 8, 9, 15, 16, 19]
words = re.findall(r'\w+', s)
elements_map = {}
for i, w in enumerate(words):
    key = w[0] if i+1 in one else w[:2]
    elements_map[key] = i + 1

print(sorted(elements_map.items(), key=lambda x: x[1]))

# 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

# 実行結果
# [('H', 1), ('He', 2), ('Li', 3), ('Be', 4), ('B', 5), ('C', 6), ('N', 7), ('O', 8), ('F', 9), ('Ne', 10), ('Na', 11), ('Mi', 12), ('Al', 13), ('Si', 14), ('P', 15), ('S', 16), ('Cl', 17), ('Ar', 18), ('K', 19), ('Ca', 20)]
