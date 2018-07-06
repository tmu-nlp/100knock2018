'''
79. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．
'''
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve
from sklearn import preprocessing
import pickle

# モデルと素性のロード
with open('model', 'rb') as f1, open('feature', 'rb') as f2:
    model = pickle.load(f1)
    feature = pickle.load(f2)

# ラベルのロード
with open('sentiment', 'rb') as f:
    label = pickle.load(f)

label_predict = model.predict(feature)
# '+1'になる確率
prob = model.predict_proba(feature)[:, 1]

# ラベルの前処理('+1','-1'の文字を数値に変換)
lb = preprocessing.LabelBinarizer()
lb.fit(label)
label = lb.transform(label).ravel()

# ある閾値の適合率、再現率、閾値を取得
precsion, recall, threshold = precision_recall_curve(label, prob)

# グラフ描画
plt.plot(precsion, recall)
plt.xlabel('precision')
plt.ylabel('recall')
plt.show()