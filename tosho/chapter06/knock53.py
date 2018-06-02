# https://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5

import sys, os
sys.path.append(os.pardir)
from common.parsers import load_corenlp_sentence

def load_nlp_sentences(file_name='./nlp.txt.xml'):
    return load_corenlp_sentence(file_name)

if __name__ == '__main__':
    import itertools

    for w in itertools.islice(load_nlp_sentences(), 50):
        print(w.word)