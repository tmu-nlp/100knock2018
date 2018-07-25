'''
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
'''
from gensim.models import word2vec
import pickle

model = word2vec.Word2Vec.load('w2v')
vec_countries = {}
for line in open('../chapter09/countries'):
    country = line.rstrip('\n')
    try:
        vec_countries[country] = model[country]
    except KeyError:
        pass

with open('result96', 'w') as f:
    for country, vector in vec_countries.items():
        f.write(f'{country}\n')
        f.write(f'{vector}\n')

with open('vec_countries', 'wb') as f:
    pickle.dump(vec_countries, f)
