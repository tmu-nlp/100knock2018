from collections import OrderedDict
from math import log
from scipy import io
from scipy import sparse
import pickle


def main():
    with open('counts.pickle', mode='rb') as f:
        print('loading count data...')
        t_c_dic = pickle.load(f)
        t_dic = pickle.load(f)
        c_dic = pickle.load(f)
        N = pickle.load(f)
        print('finish loading data.')

    t_id = OrderedDict((key, i) for i, key in enumerate(t_dic.keys()))
    c_id = OrderedDict((key, i) for i, key in enumerate(c_dic.keys()))
    # 疎行列の0行列を作成（非ゼロ要素が増える毎にメモリ確保）
    matrix = sparse.lil_matrix((len(t_id), len(c_id)))

    for t_c, tc in t_c_dic.items():
        if tc < 10:
            continue
        t, c = t_c.split()
        ppmi = max(0, log(N * tc / t_dic[t] / c_dic[c]))
        if not ppmi:
            continue
        matrix[t_id[t], c_id[c]] = ppmi

    io.savemat('ppmi_mat', {'ppmi_mat': matrix})
    with open('t_id.pickle', mode='wb') as f:
        pickle.dump(t_id, f)

if __name__ == '__main__':
    main()


''' 問
84. 単語文脈行列の作成

83の出力を利用し，単語文脈行列Xを作成せよ．
ただし，行列Xの各要素Xtcは次のように定義する．

f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
f(t,c)<10ならば，Xtc=0
ここで，PPMI(t,c)はPositive Pointwise Mutual Information（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
'''

''' 実行結果

'''
