from knock72 import *

def predict_train_data():
	log_reg = joblib.load("lr.pkl")
	train_data = joblib.load("train_data.pkl")
	vect_feature_lists = vect_features(train_data["input"])
	y_hat = log_reg.predict(vect_feature_lists)
	y_prob = log_reg.predict_proba(vect_feature_lists)
	return { "predict": y_hat, "prob": y_prob, "label": train_data["label"] }

def create_train_result(predict_dict):
	result_list = []
	predict_list = predict_dict["predict"]
	prob_list = predict_dict["prob"]
	label_list = predict_dict["label"]
	train_size = len(label_list)
	for i in range(train_size):
		if predict_list[i] == -1:
			j = 0
		else:
			j = 1
		sample_dic = { "label": label_list[i], "predict": predict_list[i], "prob": prob_list[i][j] }
		result_list.append(sample_dic)
	return result_list

if __name__ == '__main__':
	predict_dict = predict_train_data()
	train_result = create_train_result(predict_dict)
	print(train_result[:5])