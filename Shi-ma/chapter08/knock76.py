from knock72 import *
from sklearn.linear_model import LogisticRegression
import pickle



def int2label(int_):
    return '+1' if int_ == 1 else '-1'


if __name__ == '__main__':
    #load features and labels
    inputs_npz = np.load('result/inputs.npz')
    features = inputs_npz['features']
    labels = inputs_npz['labels']

    # load model
    with open('result/logistic.dump', 'rb') as logistic_in:
        logistic_model = pickle.load(logistic_in)

    # test
    predicts = logistic_model.predict(features)
    probs = logistic_model.predict_proba(features)

    with open('result/label_predict_prob.tsv', 'w') as result_out:
        for label, predict, prob in zip(labels, predicts, probs):
            print('\t'.join([int2label(label), int2label(predict), str(max(prob))]), file=result_out)
