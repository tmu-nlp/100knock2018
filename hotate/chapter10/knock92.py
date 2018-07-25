# -*- coding: utf-8 -*-
from knock90 import load_word_2_vec
from sklearn.externals import joblib
import numpy as np
from tqdm import tqdm


def calc_vec(model):
    with open('knock92_90.txt', 'w') as f:
        for line in open('knock91.txt', 'r'):
            l = line.strip().split()
            try:
                vec = model[l[1]] - model[l[0]] + model[l[2]]
                similar = model.most_similar(positive=[vec], topn=1)
            except:
                similar = [[None, 0]]
            print(f'{line.strip()} {similar[0][0]} {similar[0][1]}', file=f)


def cos_similarity():
    matrix = joblib.load('../chapter09/pca.pkl')
    vocab = joblib.load('../chapter09/vocab.pkl')
    norm = np.linalg.norm(matrix, ord=2, axis=1)
    matrix = matrix / norm[:, np.newaxis]
    words = list(vocab.keys())
    with open('knock92_85.txt', 'w') as f:
        for line in tqdm(open('knock91.txt', 'r')):
            l = line.strip().split()
            top = [None, 0]
            try:
                vec = matrix[vocab[l[1]]] - matrix[vocab[l[0]]] + matrix[vocab[l[2]]]
                for index, t in enumerate(matrix):
                    cs = np.dot(matrix[index], vec)
                    if cs > top[1]:
                        top[1] = cs
                        top[0] = words[index]
            except:
                pass
            print(f'{line.strip()} {top[0]} {top[1]}', file=f)


def main():
    cos_similarity()
    model = load_word_2_vec('word2vec')
    calc_vec(model)


if __name__ == '__main__':
    main()
