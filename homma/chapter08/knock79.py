import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn.externals import joblib


def main():
    model = joblib.load('model')
    feature = joblib.load('feature')
    sentiments = joblib.load('sentiment')

    prob = model.predict_proba(feature)[:, 1]

    pre, rec, _ = precision_recall_curve(sentiments, prob)

    plt.plot(pre, rec)
    plt.xlabel('precision')
    plt.ylabel('recall')
    plt.show()

if __name__ == '__main__':
    main()


''' 問
79. 適合率-再現率グラフの描画

ロジスティック回帰モデルの分類の閾値を変化させることで，
適合率-再現率グラフを描画せよ．
'''

''' 実行結果
'''
