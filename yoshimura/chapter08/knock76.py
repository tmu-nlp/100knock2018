'''
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ
'''
import pickle

# モデルと素性のロード
with open('model', 'rb') as f1, open('feature', 'rb') as f2:
    model = pickle.load(f1)
    feature = pickle.load(f2)

# ラベルのロード
with open('sentiment', 'rb') as f:
    label = pickle.load(f)

# 予測
label_predict = model.predict(feature)
prob = model.predict_proba(feature)

for ans, pred, prob in zip(label, label_predict, prob):
    print(f'{ans}\t{pred}\t{prob}')