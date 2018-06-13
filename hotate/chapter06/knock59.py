# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import re


def search_np(str_, list_np):
    p = re.compile(r'^\((.*?)\s(.*)\)$', re.DOTALL)
    match = p.match(str_)
    tag = match.group(1)
    words = match.group(2)

    d = 0
    w = ''
    word_list = []
    for word in words:
        if word == '(':
            w += word
            d += 1

        elif word == ')':
            w += word
            d -= 1
            if d == 0:
                word_list.append(search_np(w, list_np))
                w = ''

        elif d == 0 and word == ' ':
            continue
        else:
            w += word

    word_list.append(w)
    phrase = ' '.join(word_list)
    if tag == 'NP':
        list_np.append(phrase)
    return phrase


if __name__ == '__main__':
    tree = ET.parse('knock50.txt.xml')

    sentences = []
    for sentence in tree.iter('sentence'):
        word_list = []
        for word in sentence.iter('word'):
            word_list.append(word.text)
        if len(word_list) > 0:
            sentences.append(word_list)

    for parse in tree.iter('parse'):
        list_np = []
        search_np(parse.text.strip(), list_np)
        for line in list_np:
            print(line)


