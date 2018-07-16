from gensim.models import Word2Vec as w2v
import numpy as np
import sys, os

DICT_PATH = 'GoogleNews-vectors-negative300.bin'

def main():
    model = w2v.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)

    knock86 = model.wv['United_States']
    print('United States', knock86)

    # knock87
    knock87 = model.wv.similarity('United_States', 'U.S')
    print('sim("United States", "U.S."):', knock87)

    # knock88
    knock88 = model.wv.most_similar(positive=['England'], topn=10)
    print('10 nearest neighbor of "England":', knock88)

    # knock89
    knock89 = model.wv['Spain'] - model.wv['Madrid'] + model.wv['Athens']
    knock89 = model.wv.most_similar(positive=[knock89], topn=10)
    print('10 nearest neighbor of "Spain - Madrid + Athens":', knock89)

if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')
