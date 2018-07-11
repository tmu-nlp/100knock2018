import pickle
from collections import defaultdict
from tqdm import tqdm as tq


def main():
    t_c_dic = defaultdict(int)
    t_dic = defaultdict(int)
    c_dic = defaultdict(int)
    N = 0
    for line in tq(open('knock82_out', encoding='utf8')):
        t, cs = line.split('\t')
        t_dic[t] += 1
        for c in cs.split():
            t_c_dic[f'{t} {c}'] += 1
            c_dic[c] += 1
            N += 1
    with open('counts.pickle', mode='wb') as f:
        pickle.dump(t_c_dic, f)
        pickle.dump(t_dic, f)
        pickle.dump(c_dic, f)
        pickle.dump(N, f)


if __name__ == '__main__':
    main()


''' 問
83. 単語／文脈の頻度の計測

82の出力を利用し，以下の出現分布，および定数を求めよ．

* f(t,c): 単語tと文脈語cの共起回数
* f(t,∗): 単語tの出現回数
* f(∗,c): 文脈語cの出現回数
* N: 単語と文脈語のペアの総出現回数
'''

''' 実行結果

'''
