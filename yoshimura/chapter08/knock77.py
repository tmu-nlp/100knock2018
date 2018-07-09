'''
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，F1スコアを求めるプログラムを作成せよ．
'''
from sklearn.metrics import classification_report
import pickle

# モデルと素性のロード
with open('model', 'rb') as f1, open('feature', 'rb') as f2:
    model = pickle.load(f1)
    feature = pickle.load(f2)

# ラベルのロード
with open('sentiment', 'rb') as f:
    label = pickle.load(f)

# 予測
predict = model.predict(feature)

target_names = ['+1', '-1']
print(classification_report(label, predict, target_names=target_names))

'''
0.94
'''