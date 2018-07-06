'''
references:
http://hirotaka-hachiya.hatenablog.com/entry/2017/10/12/101858
'''

from gensim.models import word2vec
import numpy as np
import sys, os

def main():
    data_path = sys.argv[1]
    model_path = sys.argv[2]

    if os.path.exists(model_path):
        model = word2vec.Word2Vec.load(model_path)
    else:
        sentences = word2vec.LineSentence(data_path)
        model = word2vec.Word2Vec(sentences)
        model.save(model_path)
    
    # knock 86
    united_states_vec = model.wv['United_States']
    print('word representation of "United States":')
    print(united_states_vec)
    print()

    # knock 87
    us_similarity = model.wv.similarity('United_States', 'U.S')
    print('similarity of "United States" and "U.S.":')
    print(us_similarity)
    print()

    # knock 88
    words_near_england = model.wv.most_similar(positive=['England'], topn=10)
    print('10 most similar words with "England":')
    for ws in words_near_england:
        print(*ws)
    print()

    # knock 89
    trg_vec = model.wv['Spain'] - model.wv['Madrid'] + model.wv['Athens']
    words_near_trg = model.wv.most_similar(positive=[trg_vec], topn=10)
    print('10 most similar words with "Spain - Madrid + Athens":')
    for ws in words_near_trg:
        print(*ws)
    print()
    
if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')

