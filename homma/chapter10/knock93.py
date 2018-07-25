import sys


def calc_accuracy(path):
    corr_cnt = 0
    all_cnt = 0
    for line in open(path, 'r', encoding='utf8'):
        words = line.rstrip().split()
        if words[3] == words[4]:
            corr_cnt += 1
        all_cnt += 1

    return corr_cnt / all_cnt


def main():
    data_path_85 = 'knock92_85_similarity'
    data_path_90 = 'knock92_90_similarity'

    print(data_path_85 + '\naccuracy = ', end='')
    print(calc_accuracy(data_path_85))
    print(data_path_90 + '\naccuracy = ', end='')
    print(calc_accuracy(data_path_90))


if __name__ == '__main__':
    main()


''' 問
93. アナロジータスクの正解率の計算

92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
'''

''' 実行結果
knock92_85_similarity
accuracy = 0.017786561264822136
knock92_90_similarity
accuracy = 0.09486166007905138
'''
