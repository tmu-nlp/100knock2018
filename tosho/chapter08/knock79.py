from knock73 import load_sentiment_data
from sklearn.linear_model import LogisticRegression
from sklearn import metrics, model_selection
import matplotlib.pyplot as plt
from itertools import cycle

def main():
    lw = 2
    x, t = load_sentiment_data()
    colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])

    critarias = [0.1 * i for i in range(1, 11)]

    for c, color in zip(critarias, colors):
        lr = LogisticRegression(C=c)
        probas = lr.fit(x, t).decision_function(x)
        precision, recall, threshold = metrics.precision_recall_curve(t, probas)
        plt.plot(precision, recall, color=color, lw=lw, label=f'C={c:.1f}')

    # plt.plot([0.5, 1], [0.5, 1], 'k--', lw=lw)
    plt.xlim([0.5, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Precision Rate')
    plt.ylabel('Recall Rate')
    plt.title('title')
    plt.legend(loc='lower right')
    plt.show()

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')