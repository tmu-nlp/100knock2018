from knock72 import *
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    label,sosei = sosei()
    lr = LogisticRegression()
    lr.fit(sosei,label)
    pre = lr.predict(sosei)
    pro = []
    for i in lr.predict_proba(sosei):
        value = max(i[0],i[1])
        pro.append(value)
    for (x,y,z) in zip(label,pre,pro):
        print(str(x) + "\t" + str(y) + "\t" + str(z))

    