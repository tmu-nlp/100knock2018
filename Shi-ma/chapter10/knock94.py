from gensim.models import word2vec
from scipy import io
import numpy as np
import pickle


if __name__ == '__main__':
    X_100_85 = io.loadmat('../chapter09/result/knock85_result.mat')['X_100']
    X100_90 = word2vec.Word2Vec.load('result/knock90.bin')

    with open('../chapter09/result/knock83_result.dump', 'rb') as data_in:
        ids_t = pickle.load(data_in)[1]

    with open('../data/wordsim353/combined.tab', 'r') as data_in:
        with open('result/knock94_85.txt', 'w') as data_out_85, open('result/knock94_90.txt', 'w') as data_out_90:
            for num_line, line in enumerate(data_in):
                if num_line == 0:
                    print(line.strip() + ' similarity', file=data_out_85)
                    print(line.strip() + ' similarity', file=data_out_90)
                else:
                    cols = line.strip().split()[:2]
                    if not all(map(lambda x: x in ids_t.keys(), cols)) or not all(map(lambda x: x in X100_90, cols)):
                        continue
                    simi_85 = np.dot(X_100_85[ids_t[cols[0]]], X_100_85[ids_t[cols[1]]]) / (np.linalg.norm(X_100_85[ids_t[cols[0]]]) * np.linalg.norm(X_100_85[ids_t[cols[1]]]))
                    print(line.strip() + ' {}'.format(simi_85), file=data_out_85)

                    simi_90 = X100_90.similarity(cols[0], cols[1])
                    print(line.strip() + ' {}'.format(simi_90), file=data_out_90)
