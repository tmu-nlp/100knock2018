from sklearn.externals import joblib
from sklearn.decomposition import TruncatedSVD
from knock84 import PPMI_PATH

PCA_PATH = 'pca.joblib'

ppmi = joblib.load(PPMI_PATH)
pca_model = TruncatedSVD(n_components=300)
pca_mat = pca_model.fit_transform(ppmi)
joblib.dump(pca_mat, PAC_PATH)
