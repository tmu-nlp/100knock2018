from sklearn.externals import joblib
from scipy.sparse import lil_matrix

def main():
    vec = joblib.load('vocab.en')
    pca_matrix = joblib.load('pca_matrix.lil')

    vocab = vec.vocabulary_

    while True:
        query = input('input word: ').strip().lower()
        query = query.replace(' ', '_')
        token_idx = vocab.get(query)

        if token_idx == None:
            print(f'Cannot found word {query} in vocabulary')
        else:
            word_vec = pca_matrix[token_idx]
            print(word_vec)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')