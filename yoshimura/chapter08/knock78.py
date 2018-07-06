'''
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．
'''
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
import pickle
import numpy as np

# モデルと素性のロード
with open('model', 'rb') as f1, open('feature', 'rb') as f2:
    model = pickle.load(f1)
    feature = pickle.load(f2)

# ラベルのロード
with open('sentiment', 'rb') as f:
    label = pickle.load(f)

# ラベルの前処理('+1','-1'の文字を数値に変換)
lb = preprocessing.LabelBinarizer()
lb.fit(label)
label = lb.transform(label).ravel()

# 5分割交差検定
accuracy = cross_val_score(model, feature, label, cv=5, scoring='accuracy')
precision = cross_val_score(model, feature, label, cv=5, scoring='precision')
recall = cross_val_score(model, feature, label, cv=5, scoring='recall')
f1 = cross_val_score(model, feature, label, cv=5, scoring='f1')

print(f'accuracy: {np.mean(accuracy)}')
print(f'precision: {np.mean(precision)}')
print(f'recall: {np.mean(recall)}')
print(f'f1: {np.mean(f1)}')

'''
すごい時間かかる
accuracy: 0.7505170464436243
precision: 0.7535291656695116
recall: 0.7447033730664608
f1: 0.7490222443965893
'''