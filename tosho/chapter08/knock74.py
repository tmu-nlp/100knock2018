import pickle as pkl
from sys import stdin
from knock73 import load_lr_model
from knock72 import load_feat_map

def main():
    fm = load_feat_map()
    lr = load_lr_model()

    for line in stdin.readlines():
        line = line.rstrip()
        one_hots = fm.extract_one_hot(line)
        one_hots = one_hots.reshape(1, one_hots.shape[0])
        pred = lr.predict(one_hots)

        print(f'{pred} {line}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')
