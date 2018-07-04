from nltk import stem
from nltk.corpus import stopwords
from collections import defaultdict
import numpy as np
import pickle



def preprocessor(input):
    stopwords_set = set(stopwords.words('english'))
    stemmer = stem.LancasterStemmer()

    preprocessed_list = []
    for word in input.lower().split():
        if word in stopwords_set:
            continue
        else:
            lemmatized = stemmer.stem(word)
            preprocessed_list.append(lemmatized)

    return ' '.join(preprocessed_list)


def make_data(txt_file_in, mode='train'):
    inputs = []
    labels = []

    for line in txt_file_in:
        line = line.lower().strip()

        input = line[3:].strip()
        input_preprocessed = preprocessor(input)
        inputs.append(input_preprocessed)

        if mode == 'train':
            label = line.split()[0]
            labels.append(int(label))

    if mode == 'train':
        return inputs, labels
    elif mode == 'test':
        return inputs


def make_ids(inputs):
    ids = defaultdict(lambda: len(ids))
    for input in inputs:
        for token in input.split():
            ids[token]

    return dict(ids)


def create_features(inputs, ids):
    # make_features
    features = []
    for input in inputs:
        feature = np.zeros(len(ids))
        for token in input.split():
            if token not in ids.keys():
                    continue
            else:
                feature[ids[token]] += 1
        features.append(feature)

    return features


if __name__ == '__main__':
    with open('result/sentiment.txt', 'r') as txt_file_in:
        inputs, labels = make_data(txt_file_in, 'train')

    ids = make_ids(inputs)
    features = create_features(inputs, ids)

    np.savez('result/inputs.npz', features=features, labels=labels)

    with open('result/ids.dump', 'wb') as ids_out:
        pickle.dump(ids, ids_out)
