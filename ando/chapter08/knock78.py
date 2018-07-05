from knock72 import *
from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
    label,sosei = sosei()
    label = zip(*[iter(range(len(label)//5))]*5)
    sosei = zip(*[iter(range(len(sosei)//5))]*5)
    for ite in range(5):
        lr = LogisticRegression()
        sosei_hozon = sosei[ite]
        label_hozon = label[ite]
        lr.fit(sosei[ite],label[ite])
        pre = lr.predict(sosei.pop(ite))
        pro = []
        for i in lr.predict_proba(sosei.pop(ite)):
            value = max(i[0],i[1])
            pro.append(value)
        size = acc = prrsize = prr = recsize = rec = acc_hozon = prr_hozon = rec_hozon = f_hozon = 0
        for (x,y) in zip(label.pop(ite),pre):
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
        sosei.insert(ite,sosei_hozon)
        label.insert(ite,label_hozon)
        acc_hozon += acc/size
        prr_hozon += prr/prrsize
        rec_hozon += rec/recsize
        f_hozon +=  (2*(prr/prrsize)*(rec/recsize))/((prr/prrsize)+(rec/recsize))
    print(acc_hozon/5, prr_hozon/5, rec_hozon/5, f_hozon/5)

    