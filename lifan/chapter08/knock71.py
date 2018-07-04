from nltk.corpus import stopwords
from sys import argv

def stopwords_exsits(word):
	stops = set(stopwords.words('english'))
	return word.lower() in stops

if __name__ == '__main__':
	print(stopwords_exsits(argv[1]))