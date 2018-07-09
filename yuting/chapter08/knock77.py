fname_result = 'result.txt'

def score(fname):
    tp =0
    fp =0
    fn = 0
    tn = 0
    with open(fname)as f:
        for line in f:
            cols = line.split('\t')
            if len(cols) < 3:
                continue

            if cols[0] == '+1':
                if cols[1] == '+1':
                    tp += 1
                else:
                    fn += 1
            else:
                if cols[1] == '-1':
                    tn += 1
                else:
                    fp += 1
    accuracy = (tp + tn)/(tp + tn + fp + fn)
    precision = (tp)/(fp + tp)
    recall = tp /(tp + fn)
    f1 = (2 * recall * precision) / (recall + precision)

    return accuracy,precision,recall,f1

if __name__=='__main__':
    accuracy, precision, recall, f1 = score(fname_result)
    print('正解率　\t{}\n適合率　\t{}\n再現率　\t{}\nF1スコア　\t{}'.format(
    accuracy, precision, recall, f1
))

'''正解率　        0.49845722300140255
適合率　        0.49845722300140255
再現率　        1.0
F1スコア　      0.6652938974166979'''
