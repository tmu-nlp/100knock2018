from sys import stdin

def main():
    tp, fp, tn, fn = 0, 0, 0, 0
    
    for line in stdin:
        line = line.rstrip()
        gold, predict, proba = map(float, line.split('\t'))

        if gold == predict:
            if predict == 1:
                tp += 1
            else:
                tn += 1
        else:
            if predict == 1:
                fp += 1
            else:
                fn += 1
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = 2 * recall * precision / (recall + precision)

    print(f'precision: {precision:.4f} | recall: {recall:.4f} | f1: {f1:.4f}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')