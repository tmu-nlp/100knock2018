from collections import Counter
from sklearn.externals import joblib

CONTEXT_PATH = "context.txt"
COUNTER_PKL = "counter.pkl"

context = open(CONTEXT_PATH,"r",encoding="utf-8").readlines()
context_dict = {}
for idx in range(len(context)):
    t, c = text[idx].split("\t")
    c = c.strip()
    context_dict[idx] = (t, c)

f_tc = Counter([tc for tc in context_dict.values()])
f_t = Counter([tc[0] for tc in context_dict.values()])
f_c = Counter([tc[1] for tc in context_dict.values()])
N = len(context)
# N = len(f_tc) ???

joblib.dump((f_tc, f_t, f_c, N), COUNTER_PKL)