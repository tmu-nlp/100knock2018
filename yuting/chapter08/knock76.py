#正解のラベル，予測されたラベル，予測確率
from knock73 import *
import codecs
import snowballstemmer
import numpy as np

fname_sentiment = 'sentiment.txt'
fname_features = 'features.txt'
fname_theta = 'theta.npy'
fname_result = 'result.txt'

if __name__=='__main__':
    # 素性辞書の読み込み
    dict_features = load_dict_features()

    # 学習結果の読み込み
    theta = np.load(fname_theta)

    # 学習データを読み込んで予測
    with codecs.open(fname_sentiment, 'r', encoding='latin-1') as file_in, \
            open(fname_result, 'w') as file_out:

        for line in file_in:

            # 素性抽出
            data_one_x = extract_features(line[2:], dict_features)

            # 予測、結果出力
            h = hypothesis(data_one_x, theta)
            if h > 0:
                file_out.write('{}\t{}\t{}\n'.format(line[0:2], '+1', h))
            else:
                file_out.write('{}\t{}\t{}\n'.format(line[0:2], '-1', 1 - h))