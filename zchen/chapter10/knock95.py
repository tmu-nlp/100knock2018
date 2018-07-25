from knock91 import load_analogy
import numpy as np

def spearman_co(zip_gen):
    energy = 0
    n = 0
    for lhs, rhs in zip_gen:
        energy += (lhs - rhs) ** 2
        n += 1
    return 1 - (6 * energy) / n / (n*n - 1)

def pearson_co(data):
    buff = np.empty((len(data), 3))
    buff[:,:2] = data - np.mean(data)
    buff[:, 2] = buff[:, 0] - buff[:,1]
    buff[:,:2]*= buff[:,:2]
    t3 = np.sum(buff, axis = 0)
    return t3[2] / np.sqrt(t3[0] * t3[1])


if __name__ == "__main__":
    sim4 = load_analogy('knock94.txt', 4)['sim+1']
    zip_gen = ((float(t[2]), float(t[3])) for t in sim4)
    data = np.asarray(tuple(zip_gen))
    print('Spearman:', spearman_co(data))
    print('Pearson: ', pearson_co(data))
