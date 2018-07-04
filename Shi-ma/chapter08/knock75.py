from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np



def int2label(int_):
    return '+1' if int_ == 1 else '-1'


if __name__ == '__main__':
    with open('result/ids.dump', 'rb') as ids_in:
        ids = pickle.load(ids_in)
    with open('result/logistic.dump', 'rb') as logistic_in:
        logistic_model = pickle.load(logistic_in)

    weights = np.array(logistic_model.coef_[0])
    indexes = np.argsort(weights)[::-1]

    print('Top 10')
    for index in indexes[:10]:
        print('{}:\t{}'.format(list(ids.keys())[index], weights[index]))

    print('\nBottom 10')
    for index in indexes[-10:]:
        print('{}:\t{}'.format(list(ids.keys())[index], weights[index]))
