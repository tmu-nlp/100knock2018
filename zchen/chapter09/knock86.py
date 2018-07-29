from sklearn.externals import joblib
from knock82 import VOCAB_PATH
import knock85 import PCA_PATH

def main():
    vocab = joblib.load(VOCAB_PATH).vocabulary_
    pca_mat = joblib.load(PCA_PATH)

    full = vocab["United_States".lower()]
    print('vec:', pca_mat[full])

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
