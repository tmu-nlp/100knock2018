#5分割交差検定#

from knock73 import *
from knock77 import *

import codecs
import snowballstemmer
import numpy as np

fname_sentiment = 'sentiment.txt'
fname_features = 'features.txt'
fname_result = 'result78.txt'

division = 5            # データの分割数
learn_alpha = 6.0       # 学習レート
learn_count = 1000      # 学習の繰り返し数

# 素性辞書の読み込み
dict_features = load_dict_features()

# 正解データ読み込み
with codecs.open(fname_sentiment, 'r', encoding='latin-1') as file_in:
    sentiments_all = list(file_in)
    #print(sentiments_all)

# 正解データを5分割
sentiments = []
unit = int(len(sentiments_all) / division)
for i in range(5):
    sentiments.append(sentiments_all[i * unit:(i + 1) * unit])
#print(sentiments)

# 5分割交差検定
with open(fname_result, 'w') as file_out:
    for i in range(division):

        print('{}/{}'.format(i + 1, division)) #1/5

        # 学習用と検証用に正解データを分割
        data_learn = []
        for j in range(division):
            if i == j:
                data_validation = sentiments[j] #检证用1个
            else:
                data_learn += sentiments[j]

        # 学習対象の配列と極性ラベルの配列作成
        data_x, data_y = create_training_set(data_learn, dict_features)

        # 学習
        theta = learn(data_x, data_y, alpha=learn_alpha, count=learn_count)

        # 検証
        for line in data_validation:

            # 素性抽出
            data_one_x = extract_features(line[2:], dict_features)

            # 予測、結果出力
            h = hypothesis(data_one_x, theta)
            if h > 0:
                file_out.write('{}\t{}\t{}\n'.format(line[0:2], '+1', h))
            else:
                file_out.write('{}\t{}\t{}\n'.format(line[0:2], '-1', 1 - h))

# 結果表示
print('\n学習レート：{}\t学習繰り返し数：{}'.format(learn_alpha, learn_count))
accuracy, precision, recall, f1 = score(fname_result)
print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
    accuracy, precision, recall, f1
))