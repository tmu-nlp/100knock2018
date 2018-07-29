import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import KFold
from knock72 import *

def train(X, y):
  log_reg = LogisticRegression()
  log_reg.fit(X, y)
  return log_reg

def predict_train_data(log_reg, test_input_arr, test_label_arr):
  vect_feature_lists = vect_features(test_input_arr)
  y_hat = log_reg.predict(vect_feature_lists)
  y_prob = log_reg.predict_proba(vect_feature_lists)
  return { "predict": y_hat, "prob": y_prob, "label": test_label_arr }
    
if __name__ == '__main__':
  train_data = joblib.load("train_data.pkl")
  X_1D = train_data["input"]
  y = train_data["label"]

  kf = KFold(n_splits = 5, shuffle = True)
  accuracy = []
  precision = []
  recall = []
  F1 = []

  for splited_index in kf.split(X_1D):
    input_arr = np.take(X_1D, splited_index[0])
    label_arr = np.take(y, splited_index[0])
    test_input_arr = np.take(X_1D, splited_index[1])
    test_label_arr = np.take(y, splited_index[1])
    X = vect_features(input_arr)
    log_reg = train(X, label_arr)

    predict_dict = predict_train_data(log_reg, test_input_arr, test_label_arr)
    label = predict_dict["label"]
    predict = predict_dict["predict"]
    accuracy.append(accuracy_score(label, predict))
    precision.append(precision_score(label, predict))
    recall.append(recall_score(label, predict))
    F1.append(f1_score(label, predict))

  print(accuracy, precision, recall, F1)

