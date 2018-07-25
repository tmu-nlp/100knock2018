'''
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''
from gensim.models import word2vec
from tqdm import tqdm
from sklearn.externals import joblib
from sklearn.metrics.pairwise import cosine_similarity
from operator import itemgetter
import sys


def main1():
    model = word2vec.Word2Vec.load('w2v')
    with open('result92_90', 'w') as f:
        for line in tqdm(open('family', 'r')):
            w1, w2, w3, _ = line.rstrip('\n').split(' ')
            try:
                vec_w1 = model.wv[w1].reshape(1, -1)
                vec_w2 = model.wv[w2].reshape(1, -1)
                vec_w3 = model.wv[w3].reshape(1, -1)
                vec = vec_w2 - vec_w1 + vec_w3
                results = model.wv.most_similar(positive=vec)
                most_sim_word = results[0][0]
                sim_value = results[0][1]
            except KeyError:
                most_sim_word = ' '
                sim_value = -1
            f.write(line.rstrip('\n') + ' ' + most_sim_word + ' ' + str(sim_value) + '\n')


def main2():
    vocab = joblib.load('../chapter09/vocab')
    matrix_300 = joblib.load('../chapter09/matrix_300')
    id_vocab = {v: k for k, v in vocab.items()} # id : word　に変換
    with open('result92_85', 'w') as f:
        for line in tqdm(open('family', 'r')):
            w1, w2, w3, _ = line.rstrip('\n').split(' ')
            try:
                vec_w1 = matrix_300[vocab[w1]].reshape(1, -1)
                vec_w2 = matrix_300[vocab[w2]].reshape(1, -1)
                vec_w3 = matrix_300[vocab[w3]].reshape(1, -1)
                vec = vec_w2 - vec_w1 + vec_w3

                cos_sim_list = []
                for i in tqdm(range(len(vocab))):
                    cos_sim = cosine_similarity(vec, matrix_300[i].reshape(1, -1))
                    cos_sim_list.append(((i, cos_sim)))
                max_ = max(cos_sim_list, key=itemgetter(1))
                most_sim_word = id_vocab[max_[0]]
                sim_value = max_[1][0][0]
            except KeyError:
                most_sim_word = ' '
                sim_value = -1
            f.write(line.rstrip('\n') + ' ' + most_sim_word + ' ' + str(sim_value) + '\n')


if __name__ == '__main__':
    if sys.argv[1] == '90':
        main1()
    elif sys.argv[1] == '85':
        main2()