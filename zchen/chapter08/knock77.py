from sklearn.metrics import classification_report, accuracy_score
from knock76 import test_trainset


Y, Y_hat = test_trainset()
print(classification_report(Y, Y_hat))
print(f'accuracy = {accuracy_score(Y, Y_hat)}')
