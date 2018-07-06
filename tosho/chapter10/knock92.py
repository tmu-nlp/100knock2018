import sys, os
import numpy as np
from gensim.models import word2vec
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from scipy.sparse import lil_matrix
from random import randint

class Count2Vec:
    def __init__(self, size=300, window=(1,5), min_count=10):
        self.size = size
        self.window = window
        self.min_count = min_count

        self.vectorizer = None
        self.vocab = None
        self.inverse_vocab = None
        self.pca_matrix = None
    
        self.print = lambda msg: sys.stderr.write(msg+'\n')

    def fit(self, doc, hint=None):
        # cache inputs
        *doc, = doc
        
        # initialize vectorizer
        self.print('learning CountVectorizer...')
        self.vectorizer = CountVectorizer()
        self.vectorizer.fit(doc)

        self.vocab = self.vectorizer.vocabulary_
        self.inverse_vocab = {}
        for k, v in self.vocab.items():
            self.inverse_vocab[v] = k
        
        # PCA
        self.print('learning cooccurrence matrix...')
        co_matrix = self.__create_co_matrix(doc)

        self.print('learning PPMI matrix...')
        ppmi_matrix = self.__create_ppmi_matrix(co_matrix)
        
        self.print('learning PC matrix...')
        self.pca_matrix = self.__create_pca_matrix(ppmi_matrix)

        self.print('Done')

    def __create_pca_matrix(self, ppmi_matrix):
        pca = TruncatedSVD(n_components=self.size)
        pca_matrix = pca.fit_transform(ppmi_matrix)

        return pca_matrix
    
    def __create_ppmi_matrix(self, co_matrix):
        vocab_size = len(self.vocab)
        ppmi_matrix = lil_matrix(co_matrix.shape)

        N = np.sum(co_matrix)
        nt_matrix = np.sum(co_matrix, axis=1)
        nc_matrix = np.sum(co_matrix, axis=0).reshape(vocab_size,1)

        rows, cols = (co_matrix >= self.min_count).nonzero()
        for row, col in zip(rows, cols):
            ntc = co_matrix[row, col].item()
            nt = nt_matrix[row].item()
            nc = nc_matrix[col].item()

            ppmi = max(np.log2( (N * ntc) / (nt * nc) ), 0)
            if ppmi != 0:
                ppmi_matrix[row, col] = ppmi

        return ppmi_matrix

    def __create_co_matrix(self, doc):
        vocab_size = len(self.vocab)
        co_matrix = lil_matrix((vocab_size, vocab_size), dtype=np.uint8)
        get_window = lambda: randint(self.window[0], self.window[1])
    
        for t, tokens in enumerate(self.__load_tokenized_doc(self.vocab.get, doc)):
            if t % 1000 == 0:
                self.print(f'{t} line proceeded')
            
            sent_size = len(tokens)
            for idx, token in enumerate(tokens):
                # stop words が None になるため。
                if token is None:
                    continue

                window = get_window()
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
        return co_matrix

    def __load_tokenized_doc(self, vocab, doc):
        for line in doc:
            words = line.strip().split()
            *tokenized, = [vocab(w.lower()) for w in words]
            yield tokenized

    def get_wv(self, word):
        word_id = self.vocab.get(word)
        if word_id is None:
            self.print(f'word "{word}" is not found.')
            return None
        else:
            return self.pca_matrix[word_id,].reshape(self.size)
    
    def get_word(self, word_idx):
        word = self.inverse_vocab.get(word_idx)
        if word is None:
            self.print(f'id "{word_idx}" is not found.')
            return None
        else:
            return word
    
    def most_similar(self, word_or_vec, topn=10):
        if isinstance(word_or_vec, str):
            vec = self.get_wv(word_or_vec)
        elif isinstance(word_or_vec, int):
            vec = self.get_wv(self.get_word(word_or_vec))
        else:
            vec = word_or_vec

        # calculate similarity over entire matrix
        sim_matrix = np.dot([vec], self.pca_matrix.T)

        topn_words = []
        while len(topn_words) < topn:
            pos = np.unravel_index(sim_matrix.argmax(), sim_matrix.shape)
            near_word = self.get_word(pos[1])
            proba = sim_matrix[pos].item()
            topn_words.append((near_word, proba))
            sim_matrix[pos] = 0
        
        return topn_words

    def save(self, filename='model.c2v'):
        joblib.dump([self.size, self.window, self.min_count, self.vectorizer, self.pca_matrix], filename)
    
    @staticmethod
    def load(filename='model.c2v'):
        size, window, min_count, vectorizer, pca_matrix = joblib.load(filename)
        model = Count2Vec(size, window, min_count)
        model.vectorizer = vectorizer
        model.vocab = vectorizer.vocabulary_
        model.inverse_vocab = {}
        for k, v in model.vocab.items():
            model.inverse_vocab[v] = k
        model.pca_matrix = pca_matrix

        return model

def main():
    w2v_path = sys.argv[1]
    c2v_path = sys.argv[2]
    c2v_data_path = sys.argv[3] if len(sys.argv) > 3 else None

    w2v = word2vec.Word2Vec.load(w2v_path)

    if os.path.exists(c2v_path):
        c2v = Count2Vec.load(filename=c2v_path)
    else:
        sys.stderr.write('building count2vec model\n')
        c2v = Count2Vec()
        c2v.fit(open(c2v_data_path))
        c2v.save(c2v_path)
        sys.stderr.write('Done\n')

    # gold_ans = []
    # w2v_ans = []
    # c2v_ans = []
    # for line in sys.stdin:
    #     capital1, country1, capital2, country2 = line.strip().split()
        
    #     w2v_trg_vec = w2v.wv[country1] - w2v.wv[capital1] + w2v.wv[capital2]
    #     w2v_near_word = w2v.most_similar(positive=[w2v_trg_vec], topn=1)[0]
    #     c2v_trg_vec = c2v.get_wv(country1) - c2v.get_word(capital1) + c2v.get_word(capital2)
    #     c2v_near_word = c2v.most_similar(word_or_vec=c2v_trg_vec, topn=1)[0]

    #     print(*[
    #         capital1, country1, capital2, country2,
    #         w2v_near_word[0], w2v_near_word[1],
    #         c2v_near_word[0], c2v_near_word[1],
    #     ])

    #     gold_ans.append(country2)
    #     w2v_ans.append(w2v_near_word[0])
    #     c2v_ans.append(c2v_near_word[0])
    
    # w2v_acc = np.sum(gold_ans == w2v_ans) / len(gold_ans)
    # c2v_acc = np.sum(gold_ans == c2v_ans) / len(gold_ans)
    # print(f'ACC(word2vec): {w2v_acc:.2f} | ACC(count2vec): {c2v_acc:.2f}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')