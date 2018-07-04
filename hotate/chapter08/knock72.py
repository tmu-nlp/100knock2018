# -*- coding: utf-8 -*-
from knock71 import stop_word
from sklearn.feature_extraction.text import TfidfVectorizer


def fit_vectorize(text_list, vectorizer):
    vector = vectorizer.fit_transform(text_list)
    return vector


def remove_stop_word(text):
    word_list = []
    words = text.split()
    for word in words:
        if stop_word(word):
            continue
        else:
            word_list.append(word)
    return word_list


def tfidf_vectorizer():
    vectorizer = TfidfVectorizer(tokenizer=remove_stop_word)
    return vectorizer


if __name__ == '__main__':
    sentences = []
    vectorizer = tfidf_vectorizer()
    for line in open('sentiment.txt', 'r'):
        sentences.append(line[3:])
    fit_vectorize(sentences, vectorizer)
