'''
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
'''
import numpy as np
from scipy.stats import rankdata


def spearman(X, Y):
    return 1.0 - (6 * sum((X - Y) ** 2) / (len(X) ** 3 - len(X)))


def main(file_path):
    human = []
    model = []
    for line in open(file_path):
        w1, w2, human_score, model_socre = line.rstrip('\n').split('\t')
        human.append(human_score)
        model.append(model_socre)

    human_rank = rankdata(np.array(human), method='ordinal')
    model_rank = rankdata(np.array(model), method='ordinal')

    print(spearman(human_rank, model_rank))

if __name__ == '__main__':
    main('result94_90')
    main('result94_85')