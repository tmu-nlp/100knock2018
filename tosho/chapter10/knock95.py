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

    rank_human = get_rank_array(human)
    rank_w2v = get_rank_array(w2v)
    rank_c2v = get_rank_array(c2v)
    w2v_spearman = spearman(rank_human, rank_w2v)
    c2v_spearman = spearman(rank_human, rank_c2v)

    print(f'spearman | word2vec: {w2v_spearman} | count2vec: {c2v_spearman}')

def get_rank_array(l):
    ranks = [None]*len(l)
    for r, i in enumerate(np.argsort(l)):
        ranks[i] = r + 1
    return ranks

def spearman(list_a, list_b):
    D = 0
    N = len(list_a)
    for a, b in zip(list_a, list_b):
        D += (a - b)**2
    return 1 - 6 * D / (N**3 - N)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')