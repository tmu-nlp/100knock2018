from knock73 import load_lr_model
from knock72 import load_feat_map
from knock73 import load_sentiment_data

def main():
    fm = load_feat_map()
    lr = load_lr_model()
    x, t = load_sentiment_data(fm)

    p = lr.predict(x)
    pp = lr.predict_proba(x)

    for tup in zip(t, p, pp):
        a_t, a_p = tup[0], tup[1]
        a_pp = tup[2][(a_p + 1)//2] # 0 for predict -1, 1 for predict 1
        print(f'{a_t}\t{a_p}\t{a_pp}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')