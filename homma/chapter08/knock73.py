from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


def main():
    # データの読み込み
    feature = joblib.load('feature')
    sentiment = joblib.load('sentiment')

    # 学習
    model = LogisticRegression(random_state=0).fit(feature, sentiment)

    # モデルの保存
    joblib.dump(model, 'model')


if __name__ == '__main__':
    main()


''' 問
73. 学習

72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
'''

''' 実行結果
'''
