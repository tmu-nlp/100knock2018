from xml.etree import ElementTree as ET

with open('nlp.txt.xml') as fr:
    lines = fr.readlines()

root = ET.fromstringlist(lines)
for word in root.findall("document/sentences/sentence/tokens/token/word"):
    print(word.text)

'''
from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://fomalhaut.sd.tmu.ac.jp:9000')

text = 'I bought an apple at the supermaket. I am going to eat it later.'

output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,coref',
        'outputFormat': 'text'

})

print(output)
'''
