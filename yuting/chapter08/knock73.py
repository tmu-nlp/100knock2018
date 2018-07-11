#72で抽出した素性を用いて，ロジスティック回帰モデルを学習

import numpy as np 
import codecs
import snowballstemmer
from knock71 import StopWord


f_sentiment = 'sentiment.txt'
f_features = 'features.txt'
f_theta = 'theta.npy' #学習した結果のθの行列は「theta.npy」に出力します

learn_alpha = 0.6
learn_count = 1000

stemmer = snowballstemmer.stemmer('english')

def hypothesis(data_x,theta):
    return 1.0 / (1.0 + np.exp(-data_x.dot(theta)))

def cost(data_x,theta,data_y):#data_y is 正解ラベル
    m = data_y.size
    h = hypothesis(data_x,theta) #data_yの予測値の行列
    j = 1/m * np.sum(-data_y * np.log(h) -(np.ones(m)-data_y) * np.log(np.ones(m) - h))  #data_xに対して予測した結果と正解との差を算出
    return j

def gradient(data_x,theta,data_y):
    m = data_y.size
    h = hypothesis(data_x,theta)
    grad = 1/m * (h-data_y).dot(data_x)
    return grad

def extract_features(data,dict_features):
    data_one_x = np.zeros(len(dict_features)+1, dtype=np.float64)#一つのレビューに対して
    data_one_x[0] = 1
    for word in data.split(' '):
        word = word.strip()
        a = StopWord(list)
        if a.exists(str):
            continue
        word = stemmer.stemWord(word)
        try:
            data_one_x[dict_features[word]] =1
        except:
            pass

    return data_one_x

def load_dict_features():
    with codecs.open(f_features,'r',encoding='latin-1')as f_in:
        return {line.strip(): i for i,line in enumerate(f_in,start=1)}

def create_training_set(sentiments,dict_features):
    data_x = np.zeros([len(sentiments),len(dict_features) +1],dtype=np.float64)
    data_y = np.zeros(len(sentiments),dtype=np.float64)
    for i, line in enumerate(sentiments):
        data_x[i] = extract_features(line[2:],dict_features)
        if line[0:2] =='+1':
            data_y[i] = 1

    return data_x,data_y

def learn(data_x,data_y,alpha,count):
    theta = np.zeros(data_x.shape[1]) 
    c = cost(data_x,theta,data_y) #誤差
    print('\t学習開始\tcost：{}'.format(c))
    for i in range(1,count + 1):
        grad = gradient(data_x,theta,data_y)
        theta -= alpha * grad
        if i % 100 == 0:
            c = cost(data_x,theta,data_y)
            e = np.max(np.absolute(alpha * grad))
            print('\t学習中(#{})\tcost：{}\tE:{}'.format(i, c, e))
    
    c = cost(data_x, theta, data_y)
    e = np.max(np.absolute(alpha * grad))
    print('\t学習完了(#{}) \tcost：{}\tE:{}'.format(i, c, e))
    return theta

if __name__=='__main__':
    # 素性辞書の読み込み
    dict_features = load_dict_features()

    # 学習対象の行列と極性ラベルの行列作成
    with codecs.open(f_sentiment, 'r', encoding='latin-1') as file_in:
        data_x, data_y = create_training_set(list(file_in), dict_features)

    # 学習
    print('学習率：{}\t学習繰り返し数：{}'.format(learn_alpha, learn_count))
    theta = learn(data_x, data_y, alpha=learn_alpha, count=learn_count)

    # 結果を保存
    np.save(f_theta, theta)