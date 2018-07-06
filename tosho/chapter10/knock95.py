import sys
import numpy as np

def main():
    human = []
    w2v = []
    c2v = []

    for i, line in enumerate(sys.stdin):
        if i == 0:
            continue
        
        fields = line.strip().split('\t')
        human.append(-float(fields[2]))
        w2v.append(-float(fields[3]))
        c2v.append(-float(fields[4]))

    human = np.argsort(human)
    w2v = np.argsort(w2v)
    c2v = np.argsort(c2v)

    w2v_spearman = spearman(human, w2v)
    c2v_spearman = spearman(human, c2v)

    print(f'spearman | word2vec: {w2v_spearman} | count2vec: {c2v_spearman}')

def spearman(list_a, list_b):
    D = 0
    N = len(list_a)
    for a, b in zip(list_a, list_b):
        D += (a - b)**2
    return 1 - 6 * D / (N**3 + N)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')