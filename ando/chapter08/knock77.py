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
    size = acc = prrsize = prr = recsize = rec = 0
    for (x,y) in zip(label,pre):
        size += 1
        if x==y:
            acc += 1
        if y == "+1":
            prrsize += 1
            if x == "+1":
                prr += 1
        if x == "+1":
            recsize += 1
            if y == "+1":
                rec += 1
    print(acc/size,prr/prrsize,rec/recsize,(2*(prr/prrsize)*(rec/recsize))/((prr/prrsize)+(rec/recsize)))

    