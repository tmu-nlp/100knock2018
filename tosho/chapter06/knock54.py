# https://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5

import sys, os
sys.path.append(os.pardir)
from chapter06.knock53 import load_nlp_xml

if __name__ == '__main__':
    import itertools

    for w in itertools.islice(load_nlp_xml(), 50):
        print('\t'.join([w.word, w.lemma, w.pos]))