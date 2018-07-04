from knock73 import train_w
from itertools import islice
import pickle as pkl

def main(model_file='model.pkl'):
    with open(model_file, 'rb') as f:
        w = pkl.load(f)
    top_10 = islice(sorted(w.items(), key=lambda i: i[1], reverse=True), 10)
    bottom_10 = islice(sorted(w.items(), key=lambda i: i[1], reverse=False), 10)

    for i in zip(top_10, bottom_10):
        print(*i)

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