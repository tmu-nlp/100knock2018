from sklearn.model_selection import cross_validate, StratifiedKFold
from knock71 import Corpus
from sklearn.externals import joblib



def cross_valid():
    vecor = joblib.load('vecor.pkl')
    model = joblib.load('model.pkl')

    corp = Corpus()
    data = tuple(corp.hand_engineering())
    X, Y = zip(*data)
    text_X = [' '.join(x) for x in X]
    X = vecor.fit_transform(text_X)

    scoring = {
        'accuracy': 'accuracy',
        "precision": "precision",
        "recall": "recall",
        "f1": "f1"
    }
    skf = StratifiedKFold(n_splits=5, shuffle=True)

    scores = cross_validate(model, X, Y, cv=skf, scoring=scoring)

    for key, value in scores.items():
        print(f'{key} : {value.mean()}')

if __name__ == '__main__':
    cross_valid()
