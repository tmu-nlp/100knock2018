from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.externals import joblib
from knock72 import get_feature


def main():
    # モデルのロード
    model = joblib.load('model')
    vocab = joblib.load('vocab')

    # sentence = input('Sentence -> ').strip()[3:]
    f = open('sentiment.txt', encoding='utf8')
    for _ in range(124):
        next(f)
    sentence = f.readline()
    print('input\n', sentence)
    sentence = sentence.strip()[3:]
    feature = get_feature(sentence)

    vectorizer = TfidfVectorizer(vocabulary=vocab)
    feature_vec = vectorizer.fit_transform([feature]).toarray()

    predict = model.predict(feature_vec)[0]
    probability = model.predict_proba(feature_vec)[0]

    if predict == -1:
        print(f'label : negative ({probability[1] * 100:.3f}%)')
    else:
        print(f'label : positive ({probability[1] * 100:.3f}%)')


if __name__ == '__main__':
    main()


''' 問
74. 予測

73で学習したロジスティック回帰モデルを用い，
与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．
'''

''' 実行結果

'''
