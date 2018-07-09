from nltk import stem
from nltk.tokenize import RegexpTokenizer
from knock71 import stopwords_exsits
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib

def regex_str(sentence):
	tokenizer = RegexpTokenizer(r'\w+')
	stemmer = stem.PorterStemmer()
	words = tokenizer.tokenize(sentence)
	return [stemmer.stem(word) for word in words if not stopwords_exsits(word)]
	
def count_word(words):
	word_counts = defaultdict(int)
	for word in words:
		word_counts[word] += 1
	return word_counts

def create_features_with_labels(txt_path="sentiment.txt"):
	feature_lists = []
	label_list = []
	raw_result = {}
	with open(txt_path, 'r') as f:
		for line in f:
			label, sentence = line.split("\t")
			label_list.append(int(label))
			word_counts = count_word(regex_str(sentence))
			feature_lists.append(word_counts)
	raw_result["input"] = feature_lists
	raw_result["label"] = label_list
	return raw_result

def vect_features(feature_lists):
	v = DictVectorizer()
	return v.fit_transform(feature_lists)

if __name__ == '__main__':
	result = create_features_with_labels()
	print(result["input"][:5])
	print(result["label"][:5])