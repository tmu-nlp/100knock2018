import re

CHAR = 1
WORD = 2


def n_gram(n, source, mode=WORD):
    if mode == WORD:
        seq = re.findall(r'\w+', source)
    elif mode == CHAR:
        seq = re.findall(r'\S', source)

    les_len = len(seq) - n + 1
    delm = ' ' if mode == WORD else ''
    res = [delm.join(seq[i:i+n]) for i in range(les_len)]
    return res


if __name__ == '__main__':
    s = 'I am an NLPer'
    word_bigram = n_gram(2, s, WORD)
    char_bigram = n_gram(2, s, CHAR)

    print(word_bigram)
    print(char_bigram)


# 05. n - gram
# 与えられたシーケンス（文字列やリストなど）からn - gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi - gram，文字bi - gramを得よ．

# 実行結果
# ['I am', 'am an', 'an NLPer']
# ['Ia', 'am', 'ma', 'an', 'nN', 'NL', 'LP', 'Pe', 'er']
