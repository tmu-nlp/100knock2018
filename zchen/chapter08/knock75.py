from sklearn.externals import joblib


# weight_rank():
model = joblib.load('model.pkl')
vecor = joblib.load('vecor.pkl')

toks = vecor.get_feature_names()
weights = model.coef_[0].tolist()
# *pairs,
pairs = sorted(zip(toks, weights), key = lambda x:x[1])

def pnt(ps):
    for p in ps:
        print('%s\t%f' % p)

pnt(pairs[:10])
pnt(pairs[:-11:-1])
