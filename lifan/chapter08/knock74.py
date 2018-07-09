from sys import argv
from knock72 import *

def predict_sentence(sentence):
	log_reg = joblib.load("lr.pkl")
	train_data = joblib.load("train_data.pkl")
	feature_lists = train_data["input"]
	feature_lists.append(count_word(regex_str(sentence)))
	vected_sentence = vect_features(feature_lists)[-1]
	y_hat = log_reg.predict(vected_sentence)
	y_prob = log_reg.predict_proba(vected_sentence)
	return { "answer": y_hat, "pos_prob": y_prob[0][1], "neg_prob": y_prob[0][0] }

if __name__ == '__main__':
	print(predict_sentence(argv[1]))
