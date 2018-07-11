import sys
import matplotlib.pyplot as plt
from gensim.models.word2vec import Word2Vec
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
import matplotlib.cm as cm 

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

    clusters = KMeans(n_clusters=5).fit_predict(vec_list)
    vec_reduced = TSNE(n_components=2).fit_transform(vec_list)
    print(vec_reduced.shape)
    
    plt.figure(figsize=(12,9))
    plt.scatter(vec_reduced[:, 0], vec_reduced[:, 1], c=['w' for _ in clusters])
    for d, l, c in zip(vec_reduced, clusters, country_list):
        plt.text(d[0], d[1], f'{l}:{c}', fontdict={'color': cm.Paired(l)})
    plt.savefig('knock99.png')

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')