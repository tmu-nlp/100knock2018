from sklearn.externals import joblib

DICT_INDEX_T_PKL = "dict_index_t.pkl"
PCA_PPMIS_PKL = "pca_ppmis.pkl"

matrix_x300 = joblib.load(PPMIS_PKL)
dict_index_t = joblib.load(DICT_INDEX_T_PKL)

print(matrix_x300[dict_index_t['United_States']])