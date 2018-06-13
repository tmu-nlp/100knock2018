# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


tree = ET.parse('nlp.txt.xml')

for token in tree.iter('token'):
    ner = token.find('NER').text
    if ner == 'PERSON':
        name = token.find('word').text
        print(name)
