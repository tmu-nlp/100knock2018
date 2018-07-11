'''
{
python knock82.py vocab <wiki.norm.entity.en
python knock82.py co-matrix <wiki.norm.entity.en >knock82.txt
}
'''

import os
from sys import stdin, stdout, stderr
from argparse import ArgumentParser
from random import randint
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import numpy as np
from scipy.sparse import lil_matrix

def main():
    parser = ArgumentParser()
    parser.add_argument('mode', choices=['vocab', 'co-matrix'])
    arg = parser.parse_args()

    if arg.mode == 'vocab':
        build_vocab()
    elif arg.mode == 'co-matrix':
        co_matrix, vec = create_co_matrix()

        vocab_size = len(vec.vocabulary_)
        terms = np.array(list(vec.vocabulary_.keys()))
        indices = np.array(list(vec.vocabulary_.values()))
        inverse_vocab = terms[np.argsort(indices)]

        for t_idx in range(vocab_size):
            
            ctx_ids = np.argwhere(co_matrix[t_idx,].todense())
            t_token = inverse_vocab[t_idx]

            for c_idx in ctx_ids:
                c_idx = c_idx[1]
                c_token = inverse_vocab[c_idx]
                freq = co_matrix[t_idx, c_idx]
                stdout.write(f'{t_token}\t{c_token}\t{freq}\n')

def create_co_matrix(vocab_path='vocab.en', matrix_path='co_matrix.lil'):
    vectorizer = joblib.load(vocab_path)
    vocab = vectorizer.vocabulary_
    vocab_size = len(vocab)

    if os.path.exists(matrix_path):
        co_matrix = joblib.load(matrix_path)
    else:
        co_matrix = lil_matrix((vocab_size, vocab_size), dtype=np.uint8)
        for t, tokens in enumerate(load_tokenized_doc(vocab.get)):
            if t % 1000 == 0:
                stderr.write(f'{t} line proceeded\n')
            
            sent_size = len(tokens)
            for idx, token in enumerate(tokens):
                # stop words が None になるため。
                if token is None:
                    continue

                window = randint(1, 5)
                for dd in range(1, window+1):
                    li = idx - dd
                    ri = idx + dd

                    if li >= 0:
                        l_token = tokens[li]
                        if l_token is not None:
                            co_matrix[token, l_token] += 1
                    if ri < sent_size:
                        r_token = tokens[ri]
                        if r_token is not None:
                            co_matrix[token, r_token] += 1
        joblib.dump(co_matrix, matrix_path)
    
    return co_matrix, vectorizer

def load_tokenized_doc(vocab, doc=stdin):
    for line in doc:
        words = line.strip().split()
        *tokenized, = [vocab(w.lower()) for w in words]
        yield tokenized

def build_vocab(vocab_path='vocab.en'):
    vectorizer = CountVectorizer(stop_words=[])
    vectorizer.fit_transform(stdin)

    stderr.write(f'{len(vectorizer.vocabulary_)} types learned\n')
    joblib.dump(vectorizer, vocab_path)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')