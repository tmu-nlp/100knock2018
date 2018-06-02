# https://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5

import sys, os
sys.path.append(os.pardir)
from chapter06.knock53 import load_nlp_sentences
from collections import defaultdict

if __name__ == '__main__':
    tokens = list(load_nlp_sentences())
    sentences = defaultdict(list)
    for t in tokens:
        sentences[t.sentence_id].append(t)
    
