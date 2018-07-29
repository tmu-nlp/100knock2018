

def spearman(list1, list2):
    N = len(list1)
    sumD2 = sum((a - b) ** 2 for a, b in zip(list1, list2))
    return 1 - 6 * sumD2 / (N ** 3 - N)


def read_calc_spearman(path):
    human = []
    machine = []
    data = open(path, encoding='utf8')
    next(data)
    for line in data:
        line = line.strip().split('\t')
        h = 0 if line[2] == '-' else float(line[2])
        m = 0 if line[3] == '-' else float(line[3])
        human.append(h)
        machine.append(m)
    return spearman(human, machine)


def main():
    data_path_85 = 'knock94_85_similarity'
    data_path_90 = 'knock94_90_similarity'
    print('#85')
    print(read_calc_spearman(data_path_85))
    print('#90')
    print(read_calc_spearman(data_path_90))


if __name__ == '__main__':
    main()


''' 問
95. WordSimilarity-353での評価

94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
'''

''' 実行結果
#85
0.9982567281861516
#90
0.9983584440011047
'''
