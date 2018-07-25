'''
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ
'''
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.externals import joblib
from gensim.models import word2vec
from tqdm import tqdm
import sys


def main1():
    model = word2vec.Word2Vec.load('w2v')
    with open('result94_90', 'w') as f:
        for line in tqdm(open('combined.tab', 'r')):
            w1, w2, human_score = line.rstrip('\n').split('\t')

            try:
                cos_sim = model.similarity(w1, w2)
            except KeyError:
                cos_sim = -1
            f.write(f'{w1}\t{w2}\t{human_score}\t{cos_sim}' + '\n')


def main2():
    vocab = joblib.load('../chapter09/vocab')
    matrix_300 = joblib.load('../chapter09/matrix_300')
    with open('result94_85', 'w') as f:
        for line in tqdm(open('combined.tab', 'r')):
            w1, w2, human_score = line.rstrip('\n').split('\t')

            try:
                vec_w1 = matrix_300[vocab[w1]].reshape(1, -1)
                vec_w2 = matrix_300[vocab[w2]].reshape(1, -1)
                cos_sim = cosine_similarity(vec_w1, vec_w2)
            except KeyError:
                cos_sim = -1
            f.write(f'{w1}\t{w2}\t{human_score}\t{cos_sim}' + '\n')

if __name__ == '__main__':
    if sys.argv[1] == '90':
        main1()
    elif sys.argv[1] == '85':
        main2()