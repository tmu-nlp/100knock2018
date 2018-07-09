# -*- coding: utf-8 -*-
from sklearn.externals import joblib
import numpy as np


def main(line, matrix, vocab):
    line = line.strip().split('\t')
    t_index = vocab[line[0]]
    t_vec = np.sum(matrix, axis=1)
    c_vec = np.sum(matrix, axis=0).reshape(len(vocab), 1)
    t = t_vec[t_index]
    print(f'{line[0]} の出現回数 : {t}')

    for c in line[1].strip().split():
        c_index = vocab[c]
        t_c = matrix[t_index, c_index]
        cc = c_vec[c_index]

        print(f'{line[0]}, {c} の共起回数 : {t_c}')
        print(f'{c} の出現回数 : {cc}')

    N = np.sum(matrix)
    print(f'単語と文脈語のペアの総出現回数 : {N}')


if __name__ == '__main__':
    matrix = joblib.load('matrix.pkl')
    vocab = joblib.load('vocab.pkl')
    while True:
        input_ = input()
        if input_ == 'quit':
            break
        main(input_, matrix, vocab)
