import pickle
import numpy as np
from tqdm import tqdm
from gensim.models import KeyedVectors
from scipy import io


def cos_sim(v1, v2):
    'コサイン類似度を計算して返す'
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return v1 @ v2 / norm if norm else -1


def print_sim_90vec(wv, words, line, f):
    try:
        sim = wv.similarity(words[0], words[1])
        print(line.rstrip(), sim, sep='\t', file=f)
    except KeyError:
        print(line.rstrip(), '-', sep='\t', file=f)


def print_sim_85vec(t_id, ppmi, words, line, f):
    try:
        sim = cos_sim(ppmi[t_id[words[0]]], ppmi[t_id[words[1]]])
        print(line.rstrip(), sim, sep='\t', file=f)
    except KeyError:
        print(line.rstrip(), '-', sep='\t', file=f)


def main():
    import os

    data_path = 'wordsim353/combined.tab'.replace('/', os.sep)
    out_path_90 = 'knock94_90_similarity'
    out_path_85 = 'knock94_85_similarity'
    model_path = 'knock90.model'
    t_id_path = '../chapter09/t_id.pickle'.replace('/', os.sep)
    ppmi_path = '../chapter09/knock85_300'.replace('/', os.sep)
    ppmi_name = 'ppmi_mat_300'

    wv = KeyedVectors.load(model_path)

    t_id = pickle.load(open(t_id_path, 'rb'))
    ppmi = io.loadmat(ppmi_path)[ppmi_name]

    with open(out_path_90, 'w', encoding='utf8') as f90, \
            open(out_path_85, 'w', encoding='utf8') as f85:
        data = open(data_path, encoding='utf8')
        next(data)
        for line in tqdm(data):
            words = line.rstrip().split()
            print_sim_85vec(t_id, ppmi, words, line, f85)
            print_sim_90vec(wv, words, line, f90)



if __name__ == '__main__':
    main()


''' 問
94. WordSimilarity-353での類似度計算

The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''

''' 実行結果
$ head knock94_85_similarity
love    sex     6.77    0.508088756338
tiger   cat     7.35    0.760567231399
tiger   tiger   10.00   1.0
book    paper   7.46    0.588248380422
computer        keyboard        7.62    0.273144446695
computer        internet        7.58    0.404305010798
plane   car     5.77    0.545628544813
train   car     6.31    0.642044879039
telephone       communication   7.50    0.519040942471
television      radio   6.77    0.767180947397

$ head knock94_90_similarity
love    sex     6.77    0.546159
tiger   cat     7.35    0.77781
tiger   tiger   10.00   1.0
book    paper   7.46    0.552468
computer        keyboard        7.62    0.604414
computer        internet        7.58    0.657611
plane   car     5.77    0.61241
train   car     6.31    0.595338
telephone       communication   7.50    0.571471
television      radio   6.77    0.788422
'''
