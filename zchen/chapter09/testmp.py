#from multiprocessing import Pool
from pathos.multiprocessing import ProcessingPool as Pool

def f(x):
    return x*x

p = Pool()
for i in p.uimap(f, range(10)):
    print(i)
