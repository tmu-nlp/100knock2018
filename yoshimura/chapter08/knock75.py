'''
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
'''
import pickle

# モデルのロード
with open('model', 'rb') as f:
    model = pickle.load(f)

# vocavをロード
with open('vocab', 'rb') as f:
    vocab = pickle.load(f)

# 重みとインデックスをタプルにして重みの低い順にソート
weight = []
for i, w in enumerate(model.coef_.tolist()[0]):
    weight.append((i, w))
weight = sorted(weight, key=lambda x: x[1])

# 重みの低い素性トップ10
print('-----low top10-----')
for taple in weight[:10]:
    print(vocab[taple[0]])

# 重みの高い素性トップ10
print('-----high top10-----')
for taple in weight[-10:]:
    print(vocab[taple[0]])