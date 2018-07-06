from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
from knock72 import *

def train(X, y):
	log_reg = LogisticRegression()
	log_reg.fit(X, y)
	return log_reg
	
if __name__ == '__main__':
	train_data = create_features_with_labels()
	X = vect_features(train_data["input"])
	y = train_data["label"]
	trained_LR = train(X, y)
	joblib.dump(trained_LR, 'lr.pkl')
	joblib.dump(train_data, 'train_data.pkl')
	# print(trained_LR.predict(X[2]))