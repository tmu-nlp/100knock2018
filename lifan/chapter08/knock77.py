from knock76 import predict_train_data
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

if __name__ == '__main__':
	predict_dict = predict_train_data()
	label = predict_dict["label"]
	predict = predict_dict["predict"]
	    
	print(f'accuracy: {accuracy_score(label, predict)}')
	print(f'precision: {precision_score(label, predict)}')
	print(f'recall: {recall_score(label, predict)}')
	print(f'F1: {f1_score(label, predict)}')

# accuracy: 0.9414743950478335
# precision: 0.9446438692612885
# recall: 0.9379103357719002
# F1: 0.9412650602409639