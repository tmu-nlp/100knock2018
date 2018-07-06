from knock72 import *
from sklearn.linear_model import LogisticRegression
import pickle



if __name__ == '__main__':
    inputs_npz = np.load('result/inputs.npz')
    features = inputs_npz['features']

    labels = inputs_npz['labels']

    logistic = LogisticRegression()
    logistic_model = logistic.fit(features, labels)

    with open('result/logistic.dump', 'wb') as logistic_out:
        pickle.dump(logistic_model, logistic_out)
