# https://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5

import sys, os
sys.path.append(os.pardir)
from chapter06.knock53 import load_nlp_sentences

def is_person(word):
    return word.pos == 'NNP' and word.ner == 'PERSON'

if __name__ == '__main__':
    for w in load_nlp_sentences():
        if is_person(w):
            print(w.word)