'''
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．
'''
import pickle


def check_stopword(word, stopwords):
    return True if word in stopwords else False

if __name__ == '__main__':
    # ストップワードのリストを作成
    stopwords = []
    for line in open('stopwords.txt', 'r'):
        line = line.rstrip()
        stopwords.append(line)

    # ストップワードリストの保存
    with open('stopwords', 'wb') as f:
        pickle.dump(stopwords, f)

    # 関数に対するテスト
    assert check_stopword('a', stopwords)
    assert check_stopword('!', stopwords)
    assert check_stopword('to', stopwords)
    assert not check_stopword(' ', stopwords)
    assert not check_stopword('bad', stopwords)
    assert not check_stopword('nice', stopwords)


