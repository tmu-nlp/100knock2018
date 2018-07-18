from sklearn.externals import joblib
from knock82 import VOCAB_PATH
import knock85 import PCA_PATH

def main():
    vocab = joblib.load(VOCAB_PATH).vocabulary_
    pca_mat = joblib.load(PCA_PATH)

    eng_vec = vocab["England".lower()]
    similarities = np.dot(pac_mat, pca_mat[eng_vec]) #  w*w.T
    top10 = np.where(np.argsort(similarities) > len(pac_mat) - 10 )
    for i in top10:
        print(vocab[i])

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
