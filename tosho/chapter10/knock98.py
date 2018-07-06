from gensim.models.word2vec import Word2Vec
from scipy.cluster.hierarchy import linkage, dendrogram
import sys
import matplotlib.pyplot as plt

def main():
    w2v_path = sys.argv[1]
    w2v = Word2Vec.load(w2v_path)

    vec_list = []
    country_list = []
    for line in sys.stdin:
        country = line.strip()

        try:
            vec = w2v.wv.get_vector(country).reshape(w2v.vector_size)
        except:
            vec = None

        if vec is not None:
            vec_list.append(vec)
            country_list.append(country)

    z = linkage(vec_list, method='ward')
    
    plt.figure(figsize=(10,10), dpi=200)
    dendrogram(z, labels=country_list)

    plt.title('Country Clustering')
    plt.savefig('dendrogram.png')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')