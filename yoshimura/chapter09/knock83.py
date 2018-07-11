'''
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．

f(t,c): 単語tと文脈語cの共起回数
f(t,∗): 単語tの出現回数
f(∗,c): 文脈語cの出現回数
N: 単語と文脈語のペアの総出現回数
'''
from collections import defaultdict
from tqdm import tqdm
from sklearn.externals import joblib
from scipy.sparse import lil_matrix
from scipy import io
import pickle

N = 0 
vocab = joblib.load('vocab')
vocab_size = len(vocab)
matrix = lil_matrix((vocab_size, vocab_size))

# 行: 単語t, 列: 文脈語cの要素が出現頻度の行列を作成
for pair in tqdm(open('context', 'r')):
    word, c_word = pair.rstrip('\n').split('\t')
    idx_t = vocab[word]
    idx_c = vocab[c_word]
    matrix[idx_t, idx_c] += 1
    N += 1

print(f'単語と文脈語のペアの総出現回数: {N}')
joblib.dump(matrix, 'matrix')
