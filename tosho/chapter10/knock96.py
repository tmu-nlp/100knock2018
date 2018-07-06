from gensim.models.word2vec import Word2Vec
import sys

def main():
    w2v_path = sys.argv[1]
    w2v = Word2Vec.load(w2v_path)

    for line in sys.stdin:
        country = line.strip()

        try:
            vec = w2v.wv.get_vector(country)
        except:
            vec = None
        
        if vec is not None:
            print(f'{country} {vec}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')