from sklearn.externals import joblib
from knock82 import VOCAB_PATH
import knock85 import PCA_PATH

def main():
    vocab = joblib.load(VOCAB_PATH).vocabulary_
    pca_mat = joblib.load(PCA_PATH)

    eng_vec = vocab["England".lower()]
    spain = pca_mat[vocab("Spain")]
    madrid = pca_mat[vocab("Madrid")]
    athens = pac_mat[vocab("Athens")]
    vec = spain - madrid + athens
    similarities = np.dot(pac_mat, vec) #  w*w.T
    top10 = np.where(np.argsort(similarities) > len(pac_mat) - 10 )
    for i in top10:
        print(vocab[i])

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
