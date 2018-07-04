'''
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
'''
from knock71 import check_stopword
from stemming.porter2 import stem
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer


def get_feature(sentence, stopwords):
    '''sentenceからストップワードを除去しステミング処理した文を返す'''
    words = sentence.split(' ')
    result = []
    for word in words:
        if not check_stopword(word, stopwords):
            result.append(stem(word))
    return ' '.join(result)

if __name__ == '__main__':

    # stopwordのリストをロード
    with open('stopwords', 'rb') as f:
        stopwords = pickle.load(f)

    # 素性抽出
    corpus = []
    labels = []
    for line in open('sentiment.txt', 'r'):
        sentence = line.strip()[3:]
        label = line[:2]

        labels.append(label)
        corpus.append(get_feature(sentence, stopwords))

    # 文章を特徴ベクトルに変換
    vectorizer = CountVectorizer()
    feature = vectorizer.fit_transform(corpus).toarray()

    sentiment = np.array(labels)

    # featureとsentimentを保存
    with open('feature', 'wb') as f1, open('sentiment', 'wb') as f2:
        pickle.dump(feature, f1)
        pickle.dump(sentiment, f2)

    # vocabサイズを保存
    with open('vocab_size', 'wb') as f1, open('vocab', 'wb') as f2:
        pickle.dump(vectorizer.vocabulary_, f1)
        pickle.dump(vectorizer.get_feature_names(), f2)



















