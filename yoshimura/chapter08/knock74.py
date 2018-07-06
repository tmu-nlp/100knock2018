'''
74. 予測
73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
その予測確率を計算するプログラムを実装せよ．
'''
from knock72 import get_feature
from sklearn.feature_extraction.text import CountVectorizer
import pickle

if __name__ == '__main__':

    # モデルのロード
    with open('model', 'rb') as f:
        model = pickle.load(f)

    # stopwordのリストをロード
    with open('stopwords', 'rb') as f:
        stopwords = pickle.load(f)
      
    # vocabサイズをロード
    with open('vocab_size', 'rb') as f:
        vocab = pickle.load(f)

    # 入力を受け取り素性抽出
    sentence = input('Please input sentence -> ').strip()[3:]
    sent_feature = get_feature(sentence, stopwords)

    # 素性をベクトルに変換
    voctorizer = CountVectorizer(vocabulary=vocab)
    feature_vec = voctorizer.fit_transform([sent_feature]).toarray()

    # 予測
    label_predict = model.predict(feature_vec)
    prob = model.predict_proba(feature_vec)
    
    print(f'label : {label_predict[0]}')
    print(f'prob(+1): {round(prob[0][0] * 100, 3)}%')
    print(f'prob(-1): {round(prob[0][1] * 100, 3)}%')
