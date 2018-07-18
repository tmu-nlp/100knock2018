from knock71 import Corpus
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression


def train():
    vecor = joblib.load('vecor.pkl')
    model = joblib.load('model.pkl')

    corp = Corpus()
    data = tuple(corp.hand_engineering())
    X, Y = zip(*data)
    text_X = [' '.join(x) for x in X]
    X = vecor.fit_transform(text_X)

    for vec, text, tag in zip(X, text_X, Y):
        print(f'入力文 : {text.strip()}')
        print(f'予測結果 : {model.predict(vec)}', tag)
        print(f'予測確率 : {model.predict_proba(vec)}')
        print()

if __name__ == '__main__':
    train()
