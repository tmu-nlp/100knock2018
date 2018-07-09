from knock72 import *
from sklearn.linear_model import LogisticRegression
import pickle
import sys



def int2label(int_):
    return '+1' if int_ == 1 else '-1'


if __name__ == '__main__':
    # load ids_dict
    with open('result/ids.dump', 'rb') as data_ids_in:
        ids = pickle.load(data_ids_in)

    # load model
    with open('result/logistic.dump', 'rb') as logistic_in:
        logistic_model = pickle.load(logistic_in)

    # test
    with open('result/sample.txt', 'r') as txt_file_in:
        inputs = make_data(txt_file_in, 'test')
        features = create_features(inputs, ids)

    for predict, prob in zip(logistic_model.predict(features), logistic_model.predict_proba(features)):
        print('predict: {}\nproba: {}\n'.format(int2label(predict), max(prob)))
