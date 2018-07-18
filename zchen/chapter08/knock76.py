from knock71 import Corpus
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression


def test_trainset():
    vecor = joblib.load('vecor.pkl')
    model = joblib.load('model.pkl')

    corp = Corpus()
    data = tuple(corp.hand_engineering())
    X, Y = zip(*data)
    text_X = [' '.join(x) for x in X]
    X = vecor.fit_transform(text_X)
    Y_hat = model.predict(X)
    Y_prob = model.predict_proba(X)

    for vec, text, tag, y_hat, y_prob, in zip(X, text_X, Y, Y_hat, Y_prob):
        print(f'入力文 : {text.strip()}')
        print('予測結果 : ', tag, y_hat, y_prob)
        print()

    return Y, Y_hat

if __name__ == '__main__':
    test_trainset()
