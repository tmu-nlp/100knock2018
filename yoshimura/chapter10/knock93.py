'''
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
'''


def calc_accuracy(file_path):
    T = 0
    N = 0
    for line in open(file_path):
        _, _, _, ans, predict, cos_sim = line.rstrip('\n').split(' ')

        if ans == predict:
            T += 1
        if predict == 'NONE':
            N -= 1
        N += 1
    print(f'正解数: {T}')
    print(f'accuracy: {T/N}')

if __name__ == '__main__':
    print('モデル90')
    calc_accuracy('result92_90')
    print('モデル85')
    calc_accuracy('result92_85')

