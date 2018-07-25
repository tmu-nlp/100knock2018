# -*- coding: utf-8 -*-
from knock90 import load_word_2_vec
from sklearn.externals import joblib
import numpy as np
from tqdm import tqdm


def calc_vec(model):
    with open('knock94_90.txt', 'w') as f:
        for line in open('combined.tab', 'r'):
            l = line.strip().split()
            try:
                similar = model.similarity(l[0], l[1])
            except:
                similar = 0
            print(f'{line.strip()} {similar}', file=f)


def cos_similarity():
    matrix = joblib.load('../chapter09/pca.pkl')
    vocab = joblib.load('../chapter09/vocab.pkl')
    norm = np.linalg.norm(matrix, ord=2, axis=1)
    matrix = matrix / norm[:, np.newaxis]
    with open('knock94_85.txt', 'w') as f:
        for line in tqdm(open('combined.tab', 'r')):
            l = line.strip().split()
            try:
                cs = np.dot(matrix[vocab[l[0]]], matrix[vocab[l[1]]])
            except:
                cs = 0
            print(f'{line.strip()} {cs}', file=f)


if __name__ == '__main__':
    cos_similarity()
    model = load_word_2_vec('word2vec')
    calc_vec(model)
