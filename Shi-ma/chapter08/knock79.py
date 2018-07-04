from knock72 import *
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve
import pickle
import matplotlib.pyplot as plt



if __name__ == '__main__':
    # load features and labels
    inputs_npz = np.load('result/inputs.npz')
    train_npz = dict()
    test_npz = dict()
    for hoge in ['features', 'labels']:
        train_npz[hoge], test_npz[hoge] = np.split(inputs_npz[hoge], [int(len(inputs_npz[hoge]) * 0.75)])

    # train
    logistic = LogisticRegression()
    logistic_model = logistic.fit(train_npz['features'], train_npz['labels'])

    # test
    predict_probs = logistic_model.predict_proba(test_npz['features'])

    precision, recall, thresholds = precision_recall_curve(test_npz['labels'], predict_probs[:, 1])
    thresholds = np.append(thresholds, 1.0)

    plt.plot(thresholds, precision, label='precision')
    plt.xlabel('thresholds')
    plt.plot(thresholds, recall, label='recall')
    plt.ylabel('scores')
    plt.legend()
    plt.savefig('result/threshold_precision_recall.png')
