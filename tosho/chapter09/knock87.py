from sklearn.externals import joblib
from scipy.sparse import lil_matrix
import numpy as np

def main():
    vec = joblib.load('vocab.en')
    pca_matrix = joblib.load('pca_matrix.lil')

    vocab = vec.vocabulary_

    while True:
        query1 = input('input word 1: ').strip().replace(' ', '_')
        query2 = input('input word 2: ').strip().replace(' ', '_')

        query1_idx = vocab.get(query1)
        query2_idx = vocab.get(query2)

        if query1_idx == None:
            print(f'Cannot found word "{query1}" in vocabulary')
        elif query2_idx == None:
            print(f'Cannot found word "{query2}" in vocabulary')
        else:
            query1_vec = pca_matrix[query1_idx]
            query2_vec = pca_matrix[query2_idx]
            similarity = np.dot(query1_vec, query2_vec)
            print(f'similarity: {similarity}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')