from sklearn.externals import joblib


def main():
    # モデルのロード
    model = joblib.load('model')
    feature = joblib.load('feature')
    sentiments = joblib.load('sentiment')

    predicts = model.predict(feature)
    probas = model.predict_proba(feature)

    with open('knock76_ans.csv', 'w', encoding='utf8') as f:
        for corr, pred, prob in zip(sentiments, predicts, probas):
            print(corr, pred, max(prob), sep='\t', file=f)

if __name__ == '__main__':
    main()


''' 問
76. ラベル付け

学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
'''

''' 実行結果 (一部)
$ head knock76_ans.csv
-1      -1      0.861046524274
-1      -1      0.639437985622
1       -1      0.504172170659
1       1       0.786826230509
1       1       0.672499144597
-1      -1      0.805205076861
1       1       0.858196349081
1       1       0.580081718279
-1      -1      0.855033781779
-1      -1      0.731229201967
'''
