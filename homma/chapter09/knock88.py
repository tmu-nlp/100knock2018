import pickle
from knock87 import cos_sim
from scipy import io


def main():
    # 単語→IDの辞書の読み込み
    t_id = pickle.load(open('t_id.pickle', 'rb'))
    # ppmi行列読み込み
    ppmi_mat_300 = io.loadmat('knock85_300')['ppmi_mat_300']
    # ベクトル取得
    v = ppmi_mat_300[t_id['England']]
    # 全単語とのコサイン類似度を計算
    t_list = list(t_id)
    sims = [(cos_sim(v, ppmi_mat_300[i]), t_list[i]) for i in range(len(t_id))]
    # 上位十件表示
    for sim, word in sorted(sims)[-2:-12:-1]:
        print(f'{word}\t{sim}')


if __name__ == '__main__':
    main()


''' 問
88. 類似度の高い単語10件

85で得た単語の意味ベクトルを読み込み，"England"とコサイン類似度が高い10語と，
その類似度を出力せよ．
'''

''' 実行結果
Australia       0.70135616793768
France  0.6544202945232287
Germany 0.6440504355960825
Italy   0.6211067495549547
Wales   0.6208412804832883
Japan   0.6176788874514159
Scotland        0.5958710602896964
Ireland 0.5920023569145688
Europe  0.5741099418273709
India   0.5515610358476848
'''
