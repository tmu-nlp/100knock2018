from sklearn.metrics import classification_report
from sklearn.externals import joblib


def main():
    tp = fp = tn = fn = 0
    for line in open('knock76_ans.csv', encoding='utf8'):
        corr, ans, _ = line.strip().split('\t')
        if ans == '1' and corr == ans:
            tp += 1
        elif ans == '1' and corr != ans:
            fp += 1
        elif ans == '-1' and corr == ans:
            tn += 1
        else:
            fn += 1

    print('正解率\t', (tp + tn) / (tp + fp + tn + fn))
    print('正例に関する適合率\t', tp / (tp + fn))


if __name__ == '__main__':
    main()


''' 問
77. 正解率の計測

76の出力を受け取り，予測の正解率，正例に関する適合率，
再現率，F1スコアを求めるプログラムを作成せよ．
'''

''' 実行結果
正解率   0.8809791783905458
正例に関する適合率       0.8773213280810355
'''
