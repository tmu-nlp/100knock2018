# -*- coding: utf-8 -*-
import random
from scipy.sparse import lil_matrix
from sklearn.externals import joblib


def analyze(sentence, matrix, vocab):
    words = sentence.strip().split()
    new_words = []
    for i in range(len(words)):
        d = random.randint(1, 5)
        if d > i:
            ld = i
        else:
            ld = d
        if d > len(words) - (i + 1):
            rd = len(words) - (i + 1)
        else:
            rd = d
        for l in range(ld):
            matrix[vocab[words[i]], vocab[words[i - l - 1]]] += 1
        for r in range(rd):
            matrix[vocab[words[i]], vocab[words[i + r + 1]]] += 1
        l_word = " ".join(words[i - ld:i])
        r_word = " ".join(words[i + 1:i + rd + 1])
        word = f'{words[i]}\t{l_word} {r_word}'
        new_words.append(word)
    return matrix, new_words


def main():
    vocab = joblib.load('vocab.pkl')
    matrix = lil_matrix((len(vocab), len(vocab)), dtype='int8')
    with open('knock_82', 'w') as f:
        for i, sentence in enumerate(open('knock_81_100', 'r')):
            if i % 1000 == 0:
                print(i)
            matrix, new_words = analyze(sentence, matrix, vocab)
            for line in new_words:
                print(line, file=f)
    joblib.dump(matrix, 'matrix.pkl')


if __name__ == '__main__':
    main()
