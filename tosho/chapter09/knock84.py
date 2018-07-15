from sklearn.externals import joblib
import numpy as np
from scipy.sparse import lil_matrix
from tqdm import tqdm

def main():
    vec = joblib.load('vocab.en')
    co_matrix = joblib.load('co_matrix.lil')

    vocab_size = len(vec.vocabulary_)
    N = np.sum(co_matrix)

    ppmi_matrix = lil_matrix(co_matrix.shape)
    nt_matrix = np.sum(co_matrix, axis=1)
    nc_matrix = np.sum(co_matrix, axis=0).reshape(vocab_size,1)

    rows, cols = (co_matrix >= 10).nonzero()
    removed = 0
    for row, col in tqdm(zip(rows, cols),total=len(rows)):
        ntc = co_matrix[row, col].item()
        nt = nt_matrix[row].item()
        nc = nc_matrix[col].item()

        ppmi = max(np.log2( (N * ntc) / (nt * nc) ), 0)
        if ppmi == 0:
            removed += 1
        else:
            ppmi_matrix[row, col] = ppmi

    print(f'{len(rows) - removed} items calced, {removed} items removed')

    joblib.dump(ppmi_matrix, 'ppmi_matrix.lil')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')