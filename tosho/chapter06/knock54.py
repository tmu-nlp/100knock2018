# https://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5

import sys, os
sys.path.append(os.pardir)
from common.parsers import load_corenlp_xml
import xml

def load_nlp_xml(file_name='./nlp.txt.xml'):
    for elm in load_corenlp_xml(file_name):
        yield elm

if __name__ == '__main__':
    import itertools

    for w in itertools.islice(load_nlp_xml(), 50):
        print('\t'.join([w.surface, w.base, w.pos]))