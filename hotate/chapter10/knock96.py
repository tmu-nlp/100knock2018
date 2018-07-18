# -*- coding: utf-8 -*-
from gensim.models import word2vec
from sklearn.externals import joblib
import numpy as np


def extract_country():
    model = word2vec.Word2Vec.load('word2vec')
    country_dic = {}
    vec = []
    index = 0
    for country in open('country', 'r'):
        try:
            country = country.strip()
            vec.append(model[country])
            country_dic[index] = country
            index += 1
        except:
            pass
    joblib.dump(dict(country_dic), 'country_dic.pkl')
    joblib.dump(np.array(vec), 'country_vec.pkl')


if __name__ == '__main__':
    extract_country()
