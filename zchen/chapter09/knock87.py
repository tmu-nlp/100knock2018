from sklearn.externals import joblib
from knock82 import VOCAB_PATH
import knock85 import PCA_PATH

def main():
    vocab = joblib.load(VOCAB_PATH).vocabulary_
    pca_mat = joblib.load(PCA_PATH)

    full = vocab["United_States".lower()]
    brif = vocab["U.S".lower()]
    similarity = np.dot(pac_mat[full], pca_mat[brif])
    similarity /= np.sqrt(np.dot(pac_mat[full], pca_mat[full]))
    similarity /= np.sqrt(np.dot(pac_mat[brif], pca_mat[brif]))
    print('cosine similarity:', similarity)

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
