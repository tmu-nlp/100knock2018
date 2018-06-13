import sys, os
sys.path.append(os.pardir)
from chapter06.knock51 import load_nlp_word
from stemming.porter2 import stem

if __name__ == '__main__':
    import itertools

    for w in itertools.islice(load_nlp_word(), 50):
        print(f'{w}\t{stem(w)}')