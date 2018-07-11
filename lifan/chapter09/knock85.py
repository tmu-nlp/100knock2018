from sklearn.externals import joblib
from sklearn.decomposition import TruncatedSVD

PPMIS_PKL = "ppmis.pkl"
PCA_PPMIS_PKL = "pca_ppmis.pkl"

ppmis = joblib.load(PPMIS_PKL)

clf = TruncatedSVD(300)
matrix_x300 = clf.fit_transform(matrix_x)

joblib.dump(matrix_x300, PCA_PPMIS_PKL)