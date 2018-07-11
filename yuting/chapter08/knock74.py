from knock73 import *
from knock71 import StopWord

if __name__=='__main__':
    # 素性辞書の読み込み
    dict_features = load_dict_features()

    # 学習結果の読み込み
    theta = np.load(f_theta)

    # 入力
    review = input('レビューを入力してください--> ')

    # 素性抽出
    data_one_x = extract_features(review, dict_features)

    # 予測
    h = hypothesis(data_one_x, theta)
    if h > 0:
        print('label:+1 ({})'.format(h))
    else:
        print('label:-1 ({})'.format(1 - h))
