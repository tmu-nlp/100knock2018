from sklearn.metrics import precision_recall_curve
from knock71 import Corpus
from sklearn.externals import joblib
import matplotlib.pyplot as plt


def plot():
    vecor = joblib.load('vecor.pkl')
    model = joblib.load('model.pkl')

    corp = Corpus()
    data = tuple(corp.hand_engineering())
    X, Y = zip(*data)
    text_X = [' '.join(x) for x in X]
    X = vecor.fit_transform(text_X)

    precision, recall, threshold = precision_recall_curve(Y, model.predict_proba(X)[:, 1])

    plt.plot(precision, recall)
    plt.xlabel('Precision')
    plt.ylabel('Recall')

    plt.show()


if __name__ == '__main__':
    plot()
