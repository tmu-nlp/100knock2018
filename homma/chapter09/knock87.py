import numpy as np
import pickle
from scipy import io


def cos_sim(v1, v2):
    'コサイン類似度を計算して返す'
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return v1 @ v2 / norm if norm else -1


def main():
    # 単語→IDの辞書の読み込み
    with open('t_id.pickle', 'rb') as f:
        t_id = pickle.load(f)
    # ppmi行列読み込み
    ppmi_mat_300 = io.loadmat('knock85_300')['ppmi_mat_300']
    # ベクトル取得
    formal_us_vec = ppmi_mat_300[t_id['United_States']]
    short_us_vec = ppmi_mat_300[t_id['U.S']]
    # コサイン類似度を計算して表示
    print(cos_sim(formal_us_vec, short_us_vec))


if __name__ == '__main__':
    main()


''' 問
87. 単語の類似度

85で得た単語の意味ベクトルを読み込み，
"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
'''

''' 実行結果
0.836705060491
'''
