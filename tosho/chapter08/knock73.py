from knock72 import FeatureMap, load_feat_map
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle as pkl

def main():
    feat_map = load_feat_map()
    print(f'feature map loaded ({len(feat_map.id_dict)} features).')

    print('loading data... ', end='', flush=True)
    
    x, t = load_sentiment_data(feat_map)

    print(f'done (data size:{x.shape}).')

    print('learning model... ', end='', flush=True)
    lr = LogisticRegression()
    lr.fit(x, t)
    print('done.')

    score = lr.score(x, t)
    print(f'ACC: {score:.2f}')

    save_lr_model(lr)

def save_lr_model(lr, file_name='lr.pkl'):
    with open(file_name, 'wb') as f:
        pkl.dump(lr.get_params(), f)

def load_lr_model(file_name='lr.pkl'):
    with open(file_name, 'rb') as f:
        p = pkl.load(f)
        lr = LogisticRegression()
        lr.set_params(**p)
        return lr

def load_sentiment_data(feat_map, file_name='sentiment.txt'):
    x, t = [], []
    for line in open(file_name):
        feat = feat_map.extract_one_hot(line)
        label = int(line[:2])
        x.append(feat)
        t.append(label)
    return np.array(x), np.array(t)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')