# from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.externals import joblib
from statistics import mean


def main():
    model = joblib.load('model')
    feature = joblib.load('feature')
    sentiments = joblib.load('sentiment')

    scoring = ['accuracy', 'precision', 'recall', 'f1']
    result = cross_validate(model, feature, sentiments, cv=5, scoring=scoring)

    print('＞＞＞ 正解率 ＜＜＜')
    print(mean(result['test_accuracy']))
    print('＞＞＞ 適合率 ＜＜＜')
    print(mean(result['test_precision']))
    print('＞＞＞ 再現率 ＜＜＜')
    print(mean(result['test_recall']))
    print('＞＞＞ F1スコア ＜＜＜')
    print(mean(result['test_f1']))


if __name__ == '__main__':
    main()


''' 問
78. 5分割交差検定

76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，
モデルの汎化性能を測定していない．
そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
'''

''' 実行結果
＞＞＞ 正解率 ＜＜＜
0.762050057059
＞＞＞ 適合率 ＜＜＜
0.765758387448
＞＞＞ 再現率 ＜＜＜
0.755014585616
＞＞＞ F1スコア ＜＜＜
0.760329422466
'''
