from knock72 import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle



if __name__ == '__main__':
    labels = [line.split('\t')[0] for line in open('result/label_predict_prob.tsv')]
    predicts = [line.split('\t')[1] for line in open('result/label_predict_prob.tsv')]
    with open('result/Accuracy_Precision_Recall_F.txt', 'w') as result_out:
        print('Accuracy: {}\n'.format(accuracy_score(labels, predicts)), file=result_out)
        print(classification_report(labels, predicts), file=result_out)
