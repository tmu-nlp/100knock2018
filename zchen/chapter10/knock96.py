from gensim.models import KeyedVectors as w2v
from tqdm import tqdm
from pickle import dump

DICT_PATH = 'GoogleNews-vectors-negative300.bin'
model = w2v.load_word2vec_format(DICT_PATH, binary=True)

def save_w2v():
    words = []
    with open('../chapter09/countries') as fr:
        for line in fr:
            words.append(line.rstrip().replace(' ', '_'))

    vs = {}
    for t in tqdm(words, desc = 'Processing'):
        try:
            vs[t] = model.wv[t]
        except:
            print('Jump %s' % t)

    print('%d entries saved' % len(vs))
    with open('knock96.pkl', 'wb') as fw:
        dump(vs, fw)

if __name__ == "__main__":
    save_w2v()
