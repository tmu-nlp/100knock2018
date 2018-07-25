from gensim.models import word2vec
import pickle

if __name__ == '__main__':
    X_100 = word2vec.Word2Vec.load('result/knock90.bin')

    with open('../data/countries.txt', 'r') as data_in, open('result/knock96.dump', 'wb') as data_out:
        countries_vec_list = list()
        for line in data_in:
            country = line.strip().replace(' ', '_')
            if country in X_100:
                countries_vec_list.append((country, X_100[country]))

        pickle.dump(countries_vec_list, data_out)
        print('\n'.join(map(lambda x: '{}'.format(x), countries_vec_list)))
