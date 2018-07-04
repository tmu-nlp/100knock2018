import pickle as pkl
from knock73 import load_lr_model
from knock72 import load_feat_map
from itertools import islice

def main(n=10):
    fm = load_feat_map()
    lr = load_lr_model()

    w = lr.coef_[0]
    print(len(w))
    w_size = len(w)
    *top, = islice(sorted(zip(range(w_size), w), key=lambda i:i[1], reverse=True), n)
    *bottom, = islice(sorted(zip(range(w_size), w), key=lambda i:i[1], reverse=False), n)

    print(f'TOP {n}')
    for f in top:
        token = fm.get_feat_token(f[0])
        print(*[token, f[1]])

    print(f'BOTTOM {n}')
    for f in bottom:
        token = fm.get_feat_token(f[0])
        print(*[token, f[1]])

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')

'''
TOP 10
engross 2.2716935198648938
refresh 2.178785206083929
unexpect 2.0220260778136603
remark 1.7426838798561943
glorious 1.6488327105794873
smarter 1.6135908424350358
witti 1.5579981150849567
unflinch 1.5161174293199715
beauti 1.4974308015466347
warm 1.496932391645233
BOTTOM 10
bore -2.243466968269965
fail -2.0024402435299167
dull -1.9222662516530058
wast -1.8221629292873136
worst -1.8057000488732893
unless -1.7661887876808897
routin -1.763159778480813
mediocr -1.7608592702577237
suppos -1.7601755302255493
appar -1.7222198105676716
'''