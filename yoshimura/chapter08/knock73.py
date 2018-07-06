'''
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．
'''
from sklearn.linear_model import LogisticRegression
import pickle

# データをロード
with open('feature', 'rb') as f1, open('sentiment', 'rb') as f2:
    x = pickle.load(f1)
    y = pickle.load(f2)

# 学習
model = LogisticRegression(random_state=0).fit(x, y)

# モデル保存
with open('model', 'wb') as f:
    pickle.dump(model, f)





