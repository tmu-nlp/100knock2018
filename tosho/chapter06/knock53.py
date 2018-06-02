# https://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5

import sys, os
sys.path.append(os.pardir)
from common.parsers import load_corenlp_xml

def load_nlp_xml(file_name='./nlp.txt.xml'):
    return load_corenlp_xml(file_name)

if __name__ == '__main__':
    import itertools

    for w in itertools.islice(load_nlp_xml(), 50):
        print(w.word)