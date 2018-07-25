from gensim.models import KeyedVectors as w2v
from knock91 import load_analogy, write_analogy
from tqdm import tqdm
import csv

DICT_PATH = 'GoogleNews-vectors-negative300.bin'
model = w2v.load_word2vec_format(DICT_PATH, binary=True)


def load_ws353():
    with open('wordsim353/combined.csv') as fr:
        data_gen = csv.reader(fr)
        head = next(data_gen)
        return list(data_gen)

def append(data):
    for t3 in tqdm(data, desc = 'Processing'):
        sim = model.wv.similarity(t3[0], t3[1])
        t3.append('%.2f' % sim)
        yield t3

if __name__ == "__main__":
    ws353 = load_ws353()
    sim4 = list(append(ws353))
    write_analogy('knock94.txt', {'sim+1':sim4})
