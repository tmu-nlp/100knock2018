from knock73 import load_sentiment_data
from sklearn import metrics, model_selection
from sklearn.linear_model import LogisticRegression

def main():
    lr = LogisticRegression()
    x, t = load_sentiment_data()
    predicted = model_selection.cross_val_predict(lr, x, t, cv=5)

    acc = metrics.accuracy_score(t, predicted)
    cp = metrics.classification_report(t, predicted)
    print(acc)
    print(cp)

if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run('main()')