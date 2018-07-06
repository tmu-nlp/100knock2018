from gensim.models.word2vec import Word2Vec
from sklearn.cluster import KMeans
import sys

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

    country_cluster = KMeans(n_clusters=5)
    cluster_list = country_cluster.fit_predict(vec_list)

    for country, cluster in sorted(zip(country_list, cluster_list), key=lambda a:a[1]):
        print(f'{country} => {cluster}')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')