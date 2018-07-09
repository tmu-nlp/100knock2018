from nltk.corpus import stopwords



def in_stopwords(test_list):
    for word in test_list:
        yield '1' if word.lower().strip() in stopwords_set else '0'


if __name__ == '__main__':
    stopwords_set = set(stopwords.words('english'))
    test_list = ['an', 'story']

    results = [i for i in in_stopwords(test_list)]

    for result, word in zip(results, test_list):
        print(result + '\t' + word.strip())
