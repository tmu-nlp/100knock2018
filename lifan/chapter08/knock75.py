from knock72 import *

def fetch_feature_lists(feature_file="feature.txt"):
	word_lists = []
	with open(feature_file, "r") as f:
		for line in f:
			word = line.strip().split()[1]
			word_lists.append(word)
	return word_lists

if __name__ == '__main__':
	log_reg = joblib.load("lr.pkl")
	word_lists = fetch_feature_lists()
	weight_dict = {}
	for word, weight in zip(word_lists, log_reg.coef_[0]):
	    weight_dict[word] = weight

	print('----------高い素性トップ10----------')
	for key, value in sorted(weight_dict.items(),key = lambda x:x[1], reverse = True)[:10]:
	    print(f"{key} => {value}")

	print('----------低い素性トップ10----------') 
	for key, value in sorted(weight_dict.items(),key = lambda x:x[1])[:10]:
	    print(f"{key} => {value}")