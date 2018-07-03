from knock72 import extract_feat
from knock71 import StopWords
from collections import defaultdict
from numpy import sign

def label_and_feat(line, stop_word):
    label = int(line[:2])
    feats = extract_feat(line, stop_word)
    return label, feats

def add_weight(w, feats, label):
    for f in feats:
        w[f] += label

def train_w(file_name='sentiment.txt', epoch=10):
    stop_word = StopWords()
    w = defaultdict(int)
    *label_and_feats, = [label_and_feat(line, stop_word) for line in open(file_name)]
    
    highest = (-1, 0, None)
    for _ in range(epoch):
        n = 0
        failed = 0
        for label, feats in label_and_feats:
            predict = sum(w[f] for f in feats)
            if sign(predict) != label:
                add_weight(w, feats, label)
                failed += 1
            n += 1
        
        acc = 100 - failed*100/n
        print(f'epoch {_}|accuracy: {acc:.2f}%')
        if acc > highest[1]:
            highest = (_, acc, dict(w))

    print(f'Best ACC={highest[1]}, epoch {highest[0]}')
    return highest[2]

def main(file_name='sentiment.txt', epoch=10):
    train_w(file_name, epoch)

if __name__ == '__main__':
    main(epoch=100)
    # import cProfile
    # cProfile.run('main()')