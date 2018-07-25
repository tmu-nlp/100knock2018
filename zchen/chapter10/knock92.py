from gensim.models import KeyedVectors as w2v
from knock91 import load_analogy, write_analogy
from tqdm import tqdm

DICT_PATH = 'GoogleNews-vectors-negative300.bin'
model = w2v.load_word2vec_format(DICT_PATH, binary=True)

def append():
    fa = load_analogy()['family']
    for t4 in tqdm(fa, desc = 'Processing'):
        v4 = tuple(model.wv[t] for t in t4)
        tt = model.wv.most_similar(positive=[v4[1], v4[2]], negative=[v4[0]], topn=1)[0][0]
        t4.append(tt)
        yield t4

if __name__ == "__main__":
    ana5 = tuple(a for a in append())
    write_analogy('knock92.txt', {'family+1':ana5})
