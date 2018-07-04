from knock72 import *
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    label,sosei = sosei()
    lr = LogisticRegression()
    lr.fit(sosei,label)
    print(lr.coef_.tolist()[0])
    