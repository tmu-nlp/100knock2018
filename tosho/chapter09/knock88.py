from sklearn.externals import joblib
from scipy.sparse import lil_matrix
import numpy as np

def main():
    vec = joblib.load('vocab.en')
    pca_matrix = joblib.load('pca_matrix.lil')

    sim_matrix = np.dot(pca_matrix, pca_matrix.T)
    np.fill_diagonal(sim_matrix, 0)

    terms = np.array(list(vec.vocabulary_.keys()))
    indices = np.array(list(vec.vocabulary_.values()))
    inverse_vocab = terms[np.argsort(indices)]

    top_ten = {}
    while len(top_ten) < 10:
        pos = np.unravel_index(sim_matrix.argmax(), sim_matrix.shape)
        word_pair = (min(pos), max(pos))
        if word_pair not in top_ten:
            top_ten[word_pair] = sim_matrix[pos]
        sim_matrix[pos] = 0
    
    for pair, similarity in top_ten.items():
        w1 = inverse_vocab[pair[0]]
        w2 = inverse_vocab[pair[1]]

        print('\t'.join(map(str, [w1, w2, similarity])))


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')