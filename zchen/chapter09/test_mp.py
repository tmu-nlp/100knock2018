from multiprocessing import Pool
from time import sleep
from random import random

def f(x):
    sleep(random())
    return x*x

results = []
def collect_result(result):
    results.append(result)

p = Pool()
r = p.map_async(f, range(10), callback=collect_result)
r.wait()

for i in results:
    print(i)
