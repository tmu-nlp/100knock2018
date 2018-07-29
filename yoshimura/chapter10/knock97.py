
'''
97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．
'''
from sklearn.cluster import KMeans
import pickle

N = 5

with open('vec_countries', 'rb') as f:
    vec_countries = pickle.load(f)

list_vec_countries = []
list_countries = []
for country, vec in vec_countries.items():
    list_countries.append(country)
    list_vec_countries.append(vec)

predicts = KMeans(n_clusters=N).fit_predict(list_vec_countries)

category_list = [[] for _ in range(N)]

for country, category in zip(list_countries, predicts):
    category_list[category].append(country)

with open('result97', 'w') as f:
    for i, category in enumerate(category_list):
        f.write('------------\n')
        f.write(f'category: {i}\n')
        f.write('------------\n')
        for country in category:
            f.write(f'{country}\n')
        f.write('\n')


