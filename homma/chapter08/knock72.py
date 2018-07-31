from stemming.porter2 import stem # pip install stemming
from knock71 import is_stopword
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib


def get_feature(sentence):
    '文からストップワードを除去してステミングした文を返す'
    phis = []
    for word in sentence.split():
        if is_stopword(word) or len(word) == 1 or word == '--':
            continue
        phis.append(stem(word))
    return ' '.join(phis)


def create_feature():
    corpus = []
    labels = []

    for line in open('sentiment.txt', encoding='utf8'):
        label = line[:2]
        sentence = line.rstrip()[3:]
        labels.append(int(label))
        processed = get_feature(sentence)
        corpus.append(processed)

    vectorizer = TfidfVectorizer()
    # vectorizer = CountVectorizer()
    feature = vectorizer.fit_transform(corpus).toarray()
    sentiment = np.array(labels)

    # 書き出し
    joblib.dump(feature, 'feature')
    joblib.dump(sentiment, 'sentiment')
    joblib.dump(vectorizer.vocabulary_, 'vocab')
    joblib.dump(vectorizer.get_feature_names(), 'name')


if __name__ == '__main__':
    create_feature()


''' 問
72. 素性抽出

極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．
'''

''' 実行結果
'''
