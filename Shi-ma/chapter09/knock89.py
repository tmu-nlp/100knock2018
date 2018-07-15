from scipy import io
import numpy as np
import pickle


if __name__ == '__main__':
    with open('result/knock83_result.dump', 'rb') as data_in:
        ids_t = pickle.load(data_in)[1]

    X_100 = io.loadmat('result/knock85_result.mat')['X_100']

    vec_target = X_100[ids_t['Spain']] - X_100[ids_t['Madrid']] + X_100[ids_t['Athens']]
    word_simi_list = list()

    sims = np.dot(vec_target, X_100.T) / (np.linalg.norm(vec_target) * np.linalg.norm(X_100.T, axis=0))
    sim_max_10_ids = np.argsort(-sims)[1:11]
    for sim_id in sim_max_10_ids:
        print(list(ids_t.keys())[sim_id], sims[sim_id])
