from sklearn.externals import joblib
from collections import OrderedDict
import math
from scipy import sparse

COUNTER_PKL = "counter.pkl"
PPMIS_PKL = "ppmis.pkl"

f_tc,f_t,f_c,N = joblib.load(COUNTER_PKL)

dict_index_t = OrderedDict((key, i) for i, key in enumerate(f_t.keys()))
dict_index_c = OrderedDict((key, i) for i, key in enumerate(f_c.keys()))

size_t = len(dict_index_t)
size_c = len(dict_index_c)
matrix_x = sparse.lil_matrix((size_t, size_c))

for i, tc in enumerate(f_tc):
	if f_tc[tc] > 10:
		ppmi = max(math.log( ( N*f_tc[tc] ) / ( ( f_t[tc[0]] ) * ( f_c[tc[1]] ) ) ),0)
		matrix_x[dict_index_t[tc[0]], dict_index_c[tc[1]]] = ppmi

joblib.dump(ppmis, PPMIS_PKL)