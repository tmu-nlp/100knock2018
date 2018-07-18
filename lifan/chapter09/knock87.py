import numpy as np

DICT_INDEX_T_PKL = "dict_index_t.pkl"
PCA_PPMIS_PKL = "pca_ppmis.pkl"

def cos_similarity(vec_a, vec_b):
	norm_a_b = np.linalg.norm(vec_a) * np.linalg.norm(vec_b)
	if norm_a_b != 0:
		return np.dot(vec_a, vec_b) / norm_a_b
	else:
		return -1

matrix_x300 = joblib.load(PPMIS_PKL)
dict_index_t = joblib.load(DICT_INDEX_T_PKL)

vec_a = matrix_x300[dict_index_t['United_States']]
vec_b = matrix_x300[dict_index_t['U.S']]

print(cos_sim(vec_a, vec_b))