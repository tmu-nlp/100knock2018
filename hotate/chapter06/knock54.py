# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


tree = ET.parse('nlp.txt.xml')

for token in tree.iter('token'):
    word = token.find('word').text
    lemma = token.find('lemma').text
    pos = token.find('POS').text
    print(f'{word}\t{lemma}\t{pos}')
