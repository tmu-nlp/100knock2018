import sys

def main():
    n = 0
    s_w2v = 0
    s_c2v = 0
    for line in sys.stdin:
        fields = line.strip().split()
        gold, w2v, c2v = fields[3], fields[4], fields[6]

        n += 1
        if w2v.lower() == gold.lower():
            s_w2v += 1
        if c2v.lower() == gold.lower():
            s_c2v += 1
    
    acc_w2v = s_w2v / n
    acc_c2v = s_c2v / n

    print(f'ACC(word2vec): {acc_w2v:.4f} | ACC(count2vec): {acc_c2v:.4f}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')