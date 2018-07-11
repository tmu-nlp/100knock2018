# -*- coding: utf-8 -*-
from collections import defaultdict
from sklearn.externals import joblib


def country_dict():
    country_name = defaultdict(set)
    for line in open('country', 'r'):
        line = line.strip().split()
        country_name[line[0]].add(' '.join(line))
    return country_name


def make_country(line, country, vocab):
    words = line.strip().split()
    l = []
    i = 0
    while True:
        if i > len(words)-1:
            break
        if words[i] in country:
            flag = True
            for c in country[words[i]]:
                len_c = len(c.split())
                if ' '.join(words[i:i + len_c]) == c:
                    l.append('_'.join(words[i:i + len_c]))
                    vocab['_'.join(words[i:i + len_c])]
                    i += len_c
                    flag = False
                    break
            if flag:
                l.append(words[i])
                vocab[words[i]]
                i += 1
        else:
            l.append(words[i])
            vocab[words[i]]
            i += 1
    return ' '.join(l), vocab


def main():
    country = country_dict()
    vocab = defaultdict(lambda: len(vocab))
    with open('knock_81_100', 'w') as f:
        for i, line in enumerate(open('knock_80_100', 'r')):
            if i % 100000 == 0:
                print(i)
            line, vocab = make_country(line, country, vocab)
            print(line, file=f)
    joblib.dump(dict(vocab), 'vocab.pkl')


if __name__ == '__main__':
    main()
