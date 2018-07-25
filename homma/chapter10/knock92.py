import numpy as np
import pickle
from tqdm import tqdm
from gensim.models import KeyedVectors
from scipy import io


def cos_sim(v1, v2):
    'コサイン類似度を計算して返す'
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return v1 @ v2 / norm if norm else -1


def print_sim_90vec(wv, w1, w2, w3, line, f):
    try:
        vec = wv[w2] - wv[w1] + wv[w3]
        sim = wv.most_similar([vec], topn=1)
        print(line.rstrip(), *sim[0], file=f)
    except KeyError:
        print(line.rstrip(), '-', '-', file=f)


def print_sim_85vec(t_id, ppmi, w1, w2, w3, line, f):
    try:
        vec = ppmi[t_id[w2]] - ppmi[t_id[w1]] + ppmi[t_id[w3]]
        # 全単語とのコサイン類似度を計算
        t_list = list(t_id)
        sims = [(cos_sim(vec, ppmi[i]), t_list[i]) for i in range(len(t_id))]
        sim, word = max(sims)
        print(line.rstrip(), word, sim, file=f)
    except KeyError:
        print(line.rstrip(), '-', '-', file=f)


def main():
    import os

    data_path = 'knock91_family'
    out_path_90 = 'knock92_90_similarity'
    out_path_85 = 'knock92_85_similarity'
    model_path = 'knock90.model'
    t_id_path = '../chapter09/t_id.pickle'.replace('/', os.sep)
    ppmi_path = '../chapter09/knock85_300'.replace('/', os.sep)
    ppmi_name = 'ppmi_mat_300'

    wv = KeyedVectors.load(model_path)

    t_id = pickle.load(open(t_id_path, 'rb'))
    ppmi = io.loadmat(ppmi_path)[ppmi_name]

    with open(out_path_90, 'w', encoding='utf8') as f90, \
        open(out_path_85, 'w', encoding='utf8') as f85:
        for line in tqdm(open(data_path, encoding='utf8')):
            w1, w2, w3, *w, = line.rstrip().split()
            print_sim_90vec(wv, w1, w2, w3, line, f90)
            print_sim_85vec(t_id, ppmi, w1, w2, w3, line, f85)

    


if __name__ == '__main__':
    main()


''' 問
92. アナロジーデータへの適用

91で作成した評価データの各事例に対して，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
'''

''' 実行結果

'''
