'''
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には"United_States"と表現されていることに注意せよ．
'''
from sklearn.externals import joblib

vocab = joblib.load('vocab')
matrix_300 = joblib.load('matrix_300') 

vec_United_States = matrix_300[vocab['United_States']]
print(vec_United_States)