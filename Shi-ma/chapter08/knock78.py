from knock72 import *
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
import pickle



if __name__ == '__main__':
    #load features and labels
    inputs_npz = np.load('result/inputs.npz')
    features = inputs_npz['features']
    labels = inputs_npz['labels']

    logistic = LogisticRegression()

    with open('result/Accuracy_Precision_Recall_F_CV5.txt', 'w') as result_out:
        scorers = ['accuracy', 'precision', 'recall', 'f1']
        scores = [cross_val_score(logistic, features, labels, cv=5, scoring=scorer) for scorer in scorers]
        for scorer, score in zip(scorers, scores):
            print('{}\t{}'.format(scorer, score.mean()), file=result_out)
