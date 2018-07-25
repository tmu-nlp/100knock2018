from sklearn.externals import joblib
import numpy as np
from scipy.sparse import lil_matrix
from sklearn.decomposition import TruncatedSVD

def main():
    ppmi_matrix = joblib.load('ppmi_matrix.lil')

    pca_matrix = TruncatedSVD(n_components=300).fit_transform(ppmi_matrix)

    print(f'{ppmi_matrix.shape} => {pca_matrix.shape}')

    joblib.dump(pca_matrix, 'pca_matrix.lil')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')