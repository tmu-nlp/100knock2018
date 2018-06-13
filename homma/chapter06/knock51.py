from knock50 import get_nlp_iter


def get_word_iter(n=-1):
    '文の終わりには空文字を返す'
    cnt = 0
    for line in get_nlp_iter():
        for word in line.split():
            if cnt == n:
                return
            yield word.rstrip('.,;:?!')
            cnt += 1
        if cnt == n:
            return
        yield ''
        cnt += 1


if __name__ == '__main__':
    for word in get_word_iter(10):
        print(word)


''' 問
51. 単語の切り出し

空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．
ただし，文の終端では空行を出力せよ．
'''

''' 実行結果
Natural
language
processing

From
Wikipedia
the
free
encyclopedia

'''
