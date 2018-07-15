from sklearn.externals import joblib
from scipy.sparse import lil_matrix
import numpy as np

def main():
    vec = joblib.load('vocab.en')
    pca_matrix = joblib.load('pca_matrix.lil')

    vocab = vec.vocabulary_
    terms = np.array(list(vec.vocabulary_.keys()))
    indices = np.array(list(vec.vocabulary_.values()))
    inverse_vocab = terms[np.argsort(indices)]
    
    w1_idx = vocab.get('Spain')
    w2_idx = vocab.get('Madrid')
    w3_idx = vocab.get('Athens')

    trg_vec = pca_matrix[w1_idx,] - pca_matrix[w2_idx, ] + pca_matrix[w3_idx, ]
    sim_matrix = np.dot([trg_vec], pca_matrix.T)

    top_ten = {}
    while len(top_ten) < 10:
        pos = np.unravel_index(sim_matrix.argmax(), sim_matrix.shape)
        idx = pos[1]
        if idx not in top_ten:
            top_ten[idx] = sim_matrix[pos]
        sim_matrix[pos] = 0
    
    for pos, similarity in top_ten.items():
        w = inverse_vocab[pos]

        print('\t'.join(map(str, [w, similarity])))

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')