from sklearn.externals import joblib


def main():
    # モデルのロード
    model = joblib.load('model')
    name = joblib.load('name')

    weight = model.coef_[0].tolist()
    pair = list(zip(weight, name))
    pair.sort()

    print('>>> worst 10 <<<')
    for p in pair[:10]:
        print(p[1], p[0], sep='\t')
    print('>>>  top 10  <<<')
    for p in pair[:-11:-1]:
        print(p[1], p[0], sep='\t')

if __name__ == '__main__':
    main()


''' 問
75. 素性の重み

73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
'''

''' 実行結果
>>> worst 10 <<<
bad     -3.6385435171345115
bore    -3.2721612399829114
dull    -3.1551968669379336
fail    -2.629701436777182
lack    -2.5786896909641017
worst   -2.538023091400525
neither -2.4367137598081556
thing   -2.146668379580253
wast    -2.1240395454327743
joke    -2.0925947689593505
>>>  top 10  <<<
beauti  3.0416897246789554
refresh 2.8225228009832426
perform 2.5762736942272433
enjoy   2.501842553510582
entertain       2.37758265050493
best    2.364920546822657
solid   2.359493168631497
still   2.279115760154006
fun     2.278374604238736
engross 2.2754401083073335
'''
