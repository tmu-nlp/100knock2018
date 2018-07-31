import pickle
from gensim.models import KeyedVectors


def main():
    import os
    countries_path = '../chapter09/countries.txt'.replace('/', os.sep)
    model_path = 'knock90.model'
    out_path = 'knock96_country'
    wv = KeyedVectors.load(model_path)

    country_dic = {}
    vec = []
    idx = 0
    for line in open(countries_path, encoding='utf8'):
        country = line.strip().replace(' ', '_')
        try:
            vec.append(wv[country])
            country_dic[idx] = country
            idx += 1
        except KeyError:
            pass

    with open(out_path, 'wb') as f:
        pickle.dump(country_dic, f)
        pickle.dump(vec, f)

if __name__ == '__main__':
    main()


''' 問
96. 国名に関するベクトルの抽出

word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
'''

''' 実行結果

'''
