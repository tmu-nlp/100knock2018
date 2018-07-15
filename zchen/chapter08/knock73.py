from knock72 import vectorize
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression


def train():
    vecor, X, Y = vectorize()
    model = LogisticRegression()
    model.fit(X, Y)
    joblib.dump(vecor, 'vecor.pkl')
    joblib.dump(model, 'model.pkl')

if __name__ == '__main__':
    train()
