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

distances = [ cos_similarity(vec_a, matrix_x300[i]) for i in range(0, len(dict_index_t)) ]
idx_sorted = np.argsort(distances)
keys = list(dict_index_t.keys())
for index in idx_sorted[-2:-12:-1]:
	print(f'{keys[index]}\t{distances[index]}')