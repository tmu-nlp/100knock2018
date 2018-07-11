from knock92 import Count2Vec
from gensim.models.word2vec import Word2Vec
import sys

def main():
    w2v_path = sys.argv[1]
    c2v_path = sys.argv[2]

    w2v = Word2Vec.load(w2v_path)
    c2v = Count2Vec.load(c2v_path)

    for i, line in enumerate(sys.stdin):
        line = line.strip()
        
        if i == 0:
            # header
            w2v_sim = 'word2vec'
            c2v_sim = 'count2vec'
        else:
            fields = line.split('\t')

            try:
                w2v_sim = w2v.similarity(fields[0], fields[1])
            except:
                w2v_sim = -1

            try:
                c2v_sim = c2v.similarity(fields[0], fields[1])
            except:
                c2v_sim = -1

        print(f'{line}\t{w2v_sim}\t{c2v_sim}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')