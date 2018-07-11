import pickle
from knock87 import cos_sim
from scipy import io


def main():
    # 単語→IDの辞書の読み込み
    t_id = pickle.load(open('t_id.pickle', 'rb'))
    # ppmi行列読み込み
    ppmi_mat_300 = io.loadmat('knock85_300')['ppmi_mat_300']
    # ベクトル取得
    v_spain = ppmi_mat_300[t_id['Spain']]
    v_madrid = ppmi_mat_300[t_id['Madrid']]
    v_athens = ppmi_mat_300[t_id['Athens']]
    v = v_spain - v_madrid + v_athens
    # 全単語とのコサイン類似度を計算
    t_list = list(t_id)
    sims = [(cos_sim(v, ppmi_mat_300[i]), t_list[i]) for i in range(len(t_id))]
    # 上位十件表示
    for sim, word in sorted(sims)[-2:-12:-1]:
        print(f'{word}\t{sim}')


if __name__ == '__main__':
    main()


''' 問
89. 加法構成性によるアナロジー

85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''

''' 実行結果
Sweden  0.7524476293688583
Italy   0.7477475975723662
Austria 0.7300480323684855
Netherlands     0.7064037178328433
Germany 0.7025524521816249
Britain 0.6840547453815037
Rome    0.6792591037321769
Russia  0.6754670770777806
Denmark 0.6629304942473591
France  0.6614311631334332

(上位20件)
Sweden  0.7524476293688583
Italy   0.7477475975723662
Austria 0.7300480323684855
Netherlands     0.7064037178328433
Germany 0.7025524521816249
Britain 0.6840547453815037
Rome    0.6792591037321769
Russia  0.6754670770777806
Denmark 0.6629304942473591
France  0.6614311631334332
Belgium 0.6599625504961247
Poland  0.6505326645468077
Greece  0.63523971907823    ◯
Berlin  0.6211483459775878
Athens  0.6208427535245976
Japan   0.6187330625138061
Ireland 0.6183130019203915
United_Kingdom  0.6160394291549862
fought  0.6113180150236501
USA     0.6037415870668746
'''
