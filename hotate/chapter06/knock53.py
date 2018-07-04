# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


#  java -cp "/usr/local/lib/stanford-corenlp-full-2014-08-27/*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP
# -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file nlp.txt
tree = ET.parse('nlp.txt.xml')

for word in tree.iter('word'):
    print(word.text)
