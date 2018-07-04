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

'''
('liber', 28) ('1982', -22)
('engross', 22) ('unless', -21)
('tape', 21) ("wasn't", -21)
('award-worthi', 19) ('prettiest', -20)
('auster', 19) ('clunker', -19)
('unflinch', 19) ('insubstanti', -19)
('cave', 18) ('snake', -19)
('lazier', 18) ('uninspir', -18)
('batch', 18) ('makhmalbaf', -18)
('grown', 18) ('ballist', -17)
'''